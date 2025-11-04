from otree.api import *

author = 'Mart van der Kam & Anne Günther'

class C(BaseConstants):
    NAME_IN_URL = 'demographics'
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
    subsession.session.demographicsLexi = Lexicon

    session = subsession.session
    if subsession.round_number == 1:
        session.num_female_de = 0
        session.num_male_de = 0
        session.num_age_18_34_de = 0
        session.num_age_35_49_de = 0
        session.num_age_50_64_de = 0
        session.num_age_65_100_de = 0
        session.num_education_low_de = 0
        session.num_education_mid_de = 0
        session.num_education_high_de = 0


class Group(BaseGroup):
    pass


def make_likert10():
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelect,
    )


def education_choices(player):
    Lexicon = player.session.demographicsLexi
    if player.session.config['language'] == 'de':
        education_choices = [
            ["1", Lexicon.education_DE_1],
            ["2", Lexicon.education_DE_2],
            ["3", Lexicon.education_DE_3],
            ["4", Lexicon.education_DE_4],
            ["5", Lexicon.education_DE_5],
            ["6", Lexicon.education_DE_6],
            ["7", Lexicon.education_DE_7],
            ["8", Lexicon.education_DE_8],
            ["9", Lexicon.education_DE_9],
            ["10", Lexicon.education_DE_10],
            ["11", Lexicon.education_DE_11]
        ]
    else:
        education_choices = [
            ["none", Lexicon.none],
            ["obligatory", Lexicon.obligatory],
            ["high_school", Lexicon.high_school],
            ["college", Lexicon.college],
            ["university", Lexicon.university],
            ["doctor", Lexicon.doctor]
        ]

    return education_choices


def gender_choices(player):
    Lexicon = player.session.demographicsLexi
    gender_choices = [
        ["female", Lexicon.female],
        ["male", Lexicon.male],
        ["other", Lexicon.other],
        ["notsay", Lexicon.notsay]
    ]
    return gender_choices


def region_choices(player):
    Lexicon = player.session.demographicsLexi
    region_choices = [
        ["urban", Lexicon.urban],
        ["suburban", Lexicon.suburban],
        ["rural", Lexicon.rural]
    ]
    return region_choices


def income_choices(player):
    Lexicon = player.session.demographicsLexi
    income_choices = [
        ["1", Lexicon.income_quintile1],
        ["2", Lexicon.income_quintile2],
        ["3", Lexicon.income_quintile3],
        ["4", Lexicon.income_quintile4],
        ["5", Lexicon.income_quintile5]
    ]
    return income_choices

def attention_check_1_choices(player):
    Lexicon = player.session.demographicsLexi
    attention_check_1_choices = [
        ["Ford", Lexicon.ford],
        ["Volkswagen", Lexicon.volkswagen],
        ["Mercedes", Lexicon.mercedes],
        ["Toyota", Lexicon.toyota],
        ["Subaru", Lexicon.subaru],
        ]
    return attention_check_1_choices

def own_car_choices(player):
    Lexicon = player.session.demographicsLexi
    own_car_choices = [
        ["yes", Lexicon.yes],
        ["no", Lexicon.no]
    ]
    return own_car_choices

def car_type_choices(player):
    Lexicon = player.session.demographicsLexi
    car_type_choices = [
        ["gasoline", Lexicon.gasoline],
        ["diesel", Lexicon.diesel],
        ["ev", Lexicon.ev],
        ["hev", Lexicon.hev]
    ]
    return car_type_choices

def car_size_choices(player):
    Lexicon = player.session.demographicsLexi
    car_size_choices = [
        ["small", Lexicon.small],
        ["medium", Lexicon.medium],
        ["large", Lexicon.large]
    ]
    return car_size_choices

def car_size_future_choices(player):
    Lexicon = player.session.demographicsLexi
    car_size_future_choices = [
        ["small", Lexicon.small],
        ["medium", Lexicon.medium],
        ["large", Lexicon.large]
    ]
    return car_size_future_choices

def car_type_future_choices(player):
    Lexicon = player.session.demographicsLexi
    car_size_future_choices = [
        ["new_only", Lexicon.new_only],
        ["preowned_only", Lexicon.preowned_only],
        ["new_preowned", Lexicon.new_preowned]
    ]
    return car_size_future_choices

def own_car_future_choices(player):
    Lexicon = player.session.demographicsLexi
    own_car_future_choices = [
        ["yes", Lexicon.yes],
        ["no", Lexicon.no]
    ]
    return own_car_future_choices



class Player(BasePlayer):

    quota_full = models.IntegerField(initial=0)

    # Demographics
    age = models.IntegerField(min=1, max=99)
    gender = models.StringField(widget=widgets.RadioSelect,)
    education = models.StringField(widget=widgets.RadioSelect,)
    income = models.StringField(widget=widgets.RadioSelect,)
    household = models.IntegerField(min=1, max=12)
    region = models.StringField(widget=widgets.RadioSelect,)
    zip_code = models.StringField(blank=True)
    attention_check_1 = models.StringField(widget=widgets.RadioSelect,)

    # Car_questions
    own_car = models.StringField(widget=widgets.RadioSelect,)
    own_car_future = models.StringField(widget=widgets.RadioSelect,)

    # car_owner
    car_type = models.StringField(widget=widgets.RadioSelect,)
    car_size = models.StringField(widget=widgets.RadioSelect,)
    car_number = models.IntegerField(min=1, max=8)
    km_day = models.IntegerField(min=0, max=1000)
    km_year = models.IntegerField(min=0, max=100000)
    car_age = models.IntegerField(min=1, max=30)
    car_replace = models.IntegerField(min=1, max=20)
    car_size_future = models.StringField(widget=widgets.RadioSelect,)
    car_type_future = models.StringField(widget=widgets.RadioSelect,)

    # no_car_owner
    own_car_future = models.StringField(widget=widgets.RadioSelect,)

    # affect
    affect_ev = make_likert10()
    affect_ice = make_likert10()

    
# Demographics Pages class
class Demographics_1(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education']

    @staticmethod
    def error_message(player: Player, values):
        Lexicon = player.session.demographicsLexi
        if values['age'] < 18:
            return Lexicon.age_error_label

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['age', 'gender', 'education'],
            form_field_labels=[Lexicon.age_label, Lexicon.gender_label, Lexicon.education_label],
        )
    
       ## quotas: add all of this code and include for other variables

     ## once you have started a session the quotas will all be set to 0, 
     ## so add ~10-20% to the N depending on what you expect data quality to be like and be more lenient for difficult to reach groups e.g. older people
    
    @staticmethod
    def before_next_page(player: Player,timeout_happened):
        session = player.session
        participant = player.participant

        if player.gender == 'female' and session.num_female_de >= 1: # define N's for each category, if not defined here there is no quota on it, so every "diverse" person can participate
            player.quota_full = 1
            participant.quota_full = 1
        elif player.gender == 'male' and session.num_male_de >= 1:
            player.quota_full = 1
            participant.quota_full = 1
        
        age = player.age
        if 18 <= age <= 34 and session.num_age_18_34_de >= 1:
            player.quota_full = 1
        elif 35 <= age <= 49 and session.num_age_35_49_de >= 1:
            player.quota_full = 1
        elif 50 <= age <= 64 and session.num_age_50_64_de >= 1:
            player.quota_full = 1
        elif 65 <= age <= 100 and session.num_age_65_100_de >= 1:
            player.quota_full = 1

        education = player.education
        if education in ["1","2","3","4","5"] and session.num_education_low_de >= 1:
            player.quota_full = 1
        elif education in ["6","7"] and session.num_education_mid_de >= 1:
            player.quota_full = 1
        elif education in ["8","9","10","11"] and session.num_education_high_de >= 1:
            player.quota_full = 1

        participant.quota_full = player.quota_full

        ### quotas: you need to do this for all variables for which you have quotas
        participant.vars['gender'] = player.gender
        participant.vars['age'] = player.age
        participant.vars['education'] = player.education


### quotas:  add a quota full page => this makes sure that people can not participate if the quotas are full => this should be placed directly after the demographics
### you will probably get a link from the market research institute for quota fulls you can add that in the QuotaFull.html
class QuotaFull(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.quota_full == 1
    
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)


class Demographics_2(Page):
    form_model = 'player'
    form_fields = ['income', 'household', 'region', 'zip_code','attention_check_1']

    @staticmethod
    def error_message(player: Player, values):
        Lexicon = player.session.demographicsLexi
        correct = Lexicon.toyota

        if values['attention_check_1'] != correct:
            participant_id = player.participant.label or player.participant.code

            fail_url = (
                "https://www.panelservice.com/ps/se.ashx?"
                "s=6C2369B275393EA2&pid=uba25045t1&int=bq&eid=" + participant_id
            )

            # Store redirect URL
            player.participant.vars["fail_url"] = fail_url

            return Lexicon.attention_check_1_error_label

    @staticmethod
    def vars_for_template(player: Player):
        # ALWAYS include fail_url (even if None)
        return dict(
            Lexicon=player.session.demographicsLexi,
            fail_url=player.participant.vars.get("fail_url", None)
        )

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['income', 'household', 'region', 'zip_code','attention_check_1'],
            form_field_labels=[Lexicon.income_label, Lexicon.household_label, Lexicon.region_label,
                               Lexicon.zip_code_label, Lexicon.attention_check_1_label],
        )


class Car_questions(Page):
    form_model = 'player'
    form_fields = ['own_car']

    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['own_car'] = player.own_car

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['own_car'],
            form_field_labels=[Lexicon.own_car_label]
        )


class car_owner(Page):
    form_model = 'player'
    form_fields = ['car_number', 'car_type', 'car_size','km_day', 'km_year', 'car_age', 'car_replace', 'car_size_future',  'car_type_future']

    def is_displayed(player):
        return player.participant.vars['own_car'] == 'yes'
    
    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['car_size_future'] = player.car_size_future

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['car_number', 'car_type', 'car_size','km_day', 'km_year', 'car_age', 'car_replace', 'car_size_future',  'car_type_future'],
            form_field_labels=[Lexicon.car_number_label, Lexicon.car_type_label, Lexicon.car_size_label,Lexicon.km_day_label, Lexicon.km_year_label,
                               Lexicon.car_age_label, Lexicon.car_replace_label,Lexicon.car_size_future_label,Lexicon.car_type_future_label]
        )


class no_car_owner(Page):
    form_model = 'player'
    form_fields = ['own_car_future']

    def is_displayed(player):
        return player.participant.vars['own_car'] == 'no'
    
    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['own_car_future'] = player.own_car_future
        if player.participant.vars['own_car_future'] == 'no':
            player.participant.vars['car_size_future'] = 'none'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['own_car_future'],
            form_field_labels=[Lexicon.own_car_future_label]
        )
    
class future_car_owner(Page):
    form_model = 'player'
    form_fields = ['car_size_future',  'car_type_future']

    def is_displayed(player):
        return player.participant.vars['own_car'] == 'no' and player.participant.vars['own_car_future'] == 'yes'
    
    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['car_size_future'] = player.car_size_future

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['car_size_future',  'car_type_future'],
            form_field_labels=[Lexicon.car_size_future_label, Lexicon.car_type_future_label]
        )

class affect(Page):
    form_model = 'player'
    form_fields = ['affect_ev','affect_ice']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)
    
class pre_transition(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)



# Page sequence
page_sequence = [
    Demographics_1,
    QuotaFull,
    Demographics_2,
    Car_questions,
    car_owner,
    no_car_owner,
    future_car_owner,
    affect,
    pre_transition
]
