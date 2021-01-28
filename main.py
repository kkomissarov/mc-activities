from base import session
from models import ManagementCompany, Activity, IssueType


def get_or_create_mc_activity(old_activity: Activity, mc: ManagementCompany) -> Activity:
    activity = session.query(Activity) \
        .filter(Activity.mcid == mc.id) \
        .filter(Activity.name == old_activity.name) \
        .filter(Activity.icon_url == old_activity.icon_url) \
        .first()

    if not activity:
        activity = Activity(
            name=old_activity.name,
            mcid=mc.id,
            type=old_activity.type,
            icon_url=old_activity.icon_url,
            rank=old_activity.rank,
            by_default=old_activity.by_default
        )
        session.add(activity)
        session.commit()

    return activity


def main():
    activities = session.query(Activity).filter(Activity.mcid.is_(None), Activity.deleted.is_(False)).all()
    mc_list = session.query(ManagementCompany).filter(ManagementCompany.deleted.is_(False)).all()

    for mc in mc_list:
        for old_activity in activities:
            mc_issue_types_with_old_activity = session.query(IssueType) \
                .filter(IssueType.mcid == mc.id) \
                .filter(IssueType.activity_id == old_activity.id) \
                .all()

            new_activity = get_or_create_mc_activity(old_activity, mc)

            for issue_type in mc_issue_types_with_old_activity:
                issue_type.activity_id = new_activity.id
            session.commit()


if __name__ == '__main__':
    main()
