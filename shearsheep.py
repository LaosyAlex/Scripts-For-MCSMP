import minescript as mcs # type: ignore

target = mcs.player_get_targeted_entity(nbt=True)

if target is None:
    mcs.chat("No target")
else:
    nbt = str(target.nbt)

    if "Sheared" in nbt:
        mcs.chat("Found Sheared tag")
    else:
        mcs.chat("No Sheared tag found")

    if "Sheared:1b" in nbt or "Sheared:1" in nbt:
        mcs.chat("Sheared")
    else:
        mcs.chat("Has wool / not sheared")

