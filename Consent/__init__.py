from otree.api import *

author = 'Mart van der Kam & Anne Günther'

class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.session.config['language'] == 'de':
        from .lexicon_de import Lexicon
        subsession.session.myLangCode = "_de"
    elif subsession.session.config['language'] == 'sa':
        from .lexicon_sa import Lexicon
        subsession.session.myLangCode = "_sa"
    else:
        from .lexicon_usa import Lexicon
        subsession.session.myLangCode = "_usa"
    subsession.session.introLexi = Lexicon


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Consent fields
    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)

    is_mobile = models.BooleanField()


class introduction_consent(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach']
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'Lexicon': player.session.introLexi,
            "participantlabel": player.participant.label,
        }  # add http://evstudy.otree.psychologie.unibas.ch/join/kipenere?participant_label={{%PROLIFIC_PID%}} to link on prolific



# class MobileCheck(Page):
#     form_model = 'player'
#     form_fields = ['is_mobile']

#     def vars_for_template(player: Player):
#         return {
#             'Lexicon': player.session.introLexi,
#         }

#     def before_next_page(player: Player, timeout_happened):
#         if player.is_mobile:
#             # Construct the redirect URL
#             redirect_url = (
#                 f"https://www.panelservice.com/ps/se.ashx?"
#                 f"s=6C2369B275393EA2&pid=uba25045t1&int=fi&eid={player.participant.label}"
#             )
#             # Save it if you want to use later
#             player.participant.vars['redirect_url'] = redirect_url

#             # Return redirect response
#             raise redirect(redirect_url)



class MobileCheck(Page):
    form_model = 'player'
    form_fields = ['is_mobile']

    def vars_for_template(player: Player):
        return {
            'Lexicon': player.session.introLexi,
        }
        
    def before_next_page(player: Player, timeout_happened):
        # If mobile → immediately redirect to external URL
        if player.is_mobile:
            label = player.participant.label
            url = (
                "https://www.panelservice.com/ps/se.ashx?"
                "s=6C2369B275393EA2&pid=uba25045t1&int=so&eid={}"
            ).format(label)

            raise Redirect(url)


page_sequence = [
    MobileCheck,
    introduction_consent
]
