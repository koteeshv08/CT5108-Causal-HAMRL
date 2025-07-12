from smac.env import StarCraft2Env

env = StarCraft2Env(map_name="3m")
env_info = env.get_env_info()
env.reset()

for _ in range(10):
    actions = [0] * env.n_agents
    reward, terminated, _ = env.step(actions)
    print(f"Step reward: {reward}, Done: {terminated}")

env.close()
