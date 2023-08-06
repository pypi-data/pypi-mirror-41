from ipypb.progressbar import ConfigurableProgressBar as track
from ipypb.progressbar import InteractiveRange as irange
from ipypb.progressbar import ConfigurableProgressChain as chain
from ipypb.progressbar import progressbar_factory

name = "ipypb"

ipb = progressbar_factory
showprogress = track

__all__ = ['irange', 'ipb', 'track', 'chain', 'showprogress']
