from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

def format_duration(duration):
    h = (duration // 3600) % 24
    m = (duration // 60) % 60
    s = duration % 60
    if m < 10:
        m = str('0' + str(m))
    else:
        m = str(m)
    if s < 10:
        s = str('0' + str(s))
    else:
        s = str(s)
    return ("{}ч.{}м.{}с.".format(h, m, s))

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    owner_name = passcard.owner_name

    this_passcard_visits = []
    # Программируем здесь
    for visit in Visit.objects.filter(passcard=passcard):
        duration = format_duration(visit.get_duration())
        is_strange = visit.is_visit_long()
        entered_at = localtime(visit.entered_at)

        visit_card = {
            "entered_at" : entered_at,
            "duration" : duration,
            "is_strange" : is_strange 
        }

        this_passcard_visits.append(visit_card)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
