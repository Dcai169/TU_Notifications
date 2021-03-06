from TU_Notifications import notifier, checker


def find_new_updates():
    a = open("cache.txt", mode="a")
    r = open("cache.txt", mode="r")
    updates = checker.find_team_updates()
    out = ""
    if updates is not None:
        for update in updates:
            if update not in r.read():
                out += update + "\n"
                notifier.send_notification("link", "New Team Update",
                                           "{0} released".format(update),
                                           "https://firstfrc.blob.core.windows.net/frc2019/Manual/TeamUpdates/TeamUpdate{0}.pdf".format(update[12:])
                                           )
    a.write(out)
    a.close()
    r.close()
    return out
