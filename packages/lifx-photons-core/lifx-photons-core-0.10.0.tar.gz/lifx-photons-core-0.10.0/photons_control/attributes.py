from photons_app.actions import an_action
from photons_app.errors import BadOption

from input_algorithms.spec_base import NotSpecified
from input_algorithms.meta import Meta
import sys

@an_action(special_reference=True, needs_target=True)
async def get_attr(collector, target, reference, artifact, **kwargs):
    """
    Get attributes from your globes

    ``target:get_attr d073d5000000 color``

    Where ``d073d5000000`` is replaced with the serial of the device you are
    addressing and ``color`` is replaced with the attribute you want.

    This task works by looking at all the loaded LIFX binary protocol messages
    defined for the 1024 protocol and looks for ``Get<Attr>``.

    So if you want the ``color`` attribute, it will look for the ``GetColor``
    message and send that to the device and print out the reply packet we get
    back.
    """
    protocol_register = collector.configuration["protocol_register"]

    if artifact in (None, "", NotSpecified):
        raise BadOption("Please specify what you want to get\nUsage: {0} <target>:get_attr <reference> <attr_to_get>".format(sys.argv[0]))

    kls_name = "Get{0}".format("".join(part.capitalize() for part in artifact.split("_")))

    getter = None
    for messages in protocol_register.message_register(1024):
        for kls in messages.by_type.values():
            if kls.__name__ == kls_name:
                getter = kls
                break

    if getter is None:
        raise BadOption("Sorry, couldn't find the message type {0}".format(kls_name))

    photons_app = collector.configuration["photons_app"]

    extra = photons_app.extra_as_json

    if "extra_payload_kwargs" in kwargs:
        extra.update(kwargs["extra_payload_kwargs"])

    script = target.script(getter.normalise(Meta.empty(), extra))
    async for pkt, _, _ in script.run_with(reference, **kwargs):
        print("{0}: {1}".format(pkt.serial, repr(pkt.payload)))

@an_action(special_reference=True, needs_target=True)
async def set_attr(collector, target, reference, artifact, broadcast=False, **kwargs):
    """
    Set attributes on your globes

    ``target:set_attr d073d5000000 color -- '{"hue": 360, "saturation": 1, "brightness": 1}'``

    This does the same thing as ``get_attr`` but will look for ``Set<Attr>``
    message and initiates it with the options found after the ``--``.

    So in this case it will create ``SetColor(hue=360, saturation=1, brightness=1)``
    and send that to the device.
    """
    protocol_register = collector.configuration["protocol_register"]

    if artifact in (None, "", NotSpecified):
        raise BadOption("Please specify what you want to get\nUsage: {0} <target>:set_attr <reference> <attr_to_get> -- '{{<options>}}'".format(sys.argv[0]))

    kls_name = "Set{0}".format("".join(part.capitalize() for part in artifact.split("_")))

    setter = None
    for messages in protocol_register.message_register(1024):
        for kls in messages.by_type.values():
            if kls.__name__ == kls_name:
                setter = kls
                break

    if setter is None:
        raise BadOption("Sorry, couldn't find the message type {0}".format(kls_name))

    photons_app = collector.configuration["photons_app"]

    extra = photons_app.extra_as_json

    if "extra_payload_kwargs" in kwargs:
        extra.update(kwargs["extra_payload_kwargs"])

    script = target.script(setter.normalise(Meta.empty(), extra))
    async for pkt, _, _ in script.run_with(reference, broadcast=broadcast):
        print("{0}: {1}".format(pkt.serial, repr(pkt.payload)))
