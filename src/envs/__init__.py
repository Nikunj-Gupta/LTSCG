from functools import partial
from smac.env import MultiAgentEnv, StarCraft2Env
import sys
import os
from .gather import GatherEnv
from .gymma import GymmaWrapper

def env_fn(env, **kwargs) -> MultiAgentEnv:
    return env(**kwargs)

def gymma_fn(**kwargs) -> MultiAgentEnv:
    assert "common_reward" in kwargs and "reward_scalarisation" in kwargs
    return GymmaWrapper(**kwargs)

REGISTRY = {}
REGISTRY["sc2"] = partial(env_fn, env=StarCraft2Env)
REGISTRY["gather"] = partial(env_fn, env=GatherEnv)
REGISTRY["gymma"] = gymma_fn 

if sys.platform == "linux":
    os.environ.setdefault("SC2PATH",
                          os.path.join("~", "StarCraftII"))
