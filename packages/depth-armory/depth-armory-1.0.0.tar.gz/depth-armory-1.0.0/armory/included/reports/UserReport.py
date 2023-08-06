#!/usr/bin/python
from armory.database.repositories import (
    BaseDomainRepository,
    UserRepository,
    CredRepository,
)
from armory.included.ReportTemplate import ReportTemplate
import pdb

class Report(ReportTemplate):
    """
    This report displays data related to discovered user accounts.
    """

    name = "UserReport"
    markdown = ["-", "--"]

    def __init__(self, db):

        self.BaseDomain = BaseDomainRepository(db)
        self.User = UserRepository(db)
        self.Cred = CredRepository(db)

    def set_options(self):

        super(Report, self).set_options()

        self.options.add_argument(
            "-u1",
            "--usernames_passwords",
            help="Prints out username/password pairs",
            action="store_true",
        )
        self.options.add_argument(
            "-u2",
            "--emails_passwords",
            help="Prints out email/password pairs",
            action="store_true",
        )
        self.options.add_argument(
            "-u3", "--emails", help="Prints out e-mail addresses", action="store_true"
        )
        self.options.add_argument(
            "-u4", "--accounts", help="Prints out user accounts", action="store_true"
        )
        self.options.add_argument(
            "-u5", "--full", help="Prints out full user data", action="store_true"
        )
        self.options.add_argument(
            '-t', '--title', help="Add title to the sections of results", action="store_true"
        )

    def run(self, args):

        results = []
        qry, model = self.BaseDomain.get_query()
        if args.scope == 'active':
            domains = qry.filter_by(in_scope=True).order_by(model.domain).all()
        elif args.scope == 'passive':
            domains = qry.filter_by(passive_scope=True).order_by(model.domain).all()
        else:
            domains = qry.order_by(model.domain).all()
        
        for d in domains:
            if args.title and d.users:
                results.append('{}'.format(d.domain))
            
            if args.emails:
                emails = sorted([u.email.lower() for u in d.users if u.email])
                if args.title:
                    results += ['\t{}'.format(e) for e in emails]
                else:
                    results += ['{}'.format(e) for e in emails]
            elif args.accounts:
                emails = sorted([u.email.lower() for u in d.users if u.email])
                if args.title:
                    results += ['\t{}'.format(e.split("@")[0]) for e in emails]
                else:
                    results += ['{}'.format(e.split("@")[0]) for e in emails]

            elif args.full:
                for user in d.users:
                    results.append(
                        "{}|{}|{}|{}".format(
                            user.first_name, user.last_name, user.email, user.job_title
                    )
                )
            else:
                 for user in d.users:
                    for cred in user.creds:
                        if cred.password and cred.password != "None":
                            if args.emails_passwords:
                                txt = "%s:%s" % (user.email, cred.password)

                            elif args.usernames_passwords:
                                txt = "%s:%s" % (
                                    user.email.split("@")[0],
                                    cred.password,
                                )

                            if txt not in results:
                                results.append(txt)
    
        self.process_output(results, args)
