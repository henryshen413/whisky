import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView
from whiskydatabase.models import *

def distillery_list():
    distillery_list = Distillery.objects.filter(is_active=True).distinct()
    return {'distillery_list': distillery_list}

class HomeView(ListView):
    model = WhiskyInfo
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class WhiskyListView(ListView):
    model = WhiskyInfo
    template_name = "whisky_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DistilleryMapView(TemplateView):
    template_name = "whiskymap.html"

class DistilleryListView(ListView):
    model = Distillery
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DistilleryView(DetailView):
    model = Distillery
    template_name = "home.html"

class WhiskyView(DetailView):
    template_name = "whisky_info.html"
    model = WhiskyInfo
    slug_url_kwarg = "whisky_slug"
    context_object_name = "whisky_detail"

    def post(self, request, *args, **kwargs):
        if request.POST.get('comment') : 
            content = request.POST.get('comment')
            rating = request.POST['myRating']
            p_choice = "Public"

            if request.POST.get('publish_choice'):
                p_choice = "Private"
            
            if rating is not None:
                if not rating:
                    rating = 0

                comment = Comment.objects.create(
                        note = content,
                        user = self.request.user,
                        publish_choice = p_choice,
                        whisky = self.object,
                        rating = rating
                    )
                
                comment.save()

            return HttpResponseRedirect('/whisky/{}/#r'.format(self.object.slug))

        elif request.POST.get('comment-edit'): 
            c_id = request.POST.get('comment-id')
            comment = Comment.objects.filter(id=c_id).last()
            
            content = request.POST.get('comment-edit')
            rating = request.POST['myRating-edit']
            p_choice = "Public"

            if request.POST.get('publish_choice'):
                p_choice = "Private"
            
            if rating is not None:
                if not rating:
                    rating = 0

                comment.note = content
                comment.rating = rating
                comment.publish_choice = p_choice
                
                comment.save()

            return HttpResponseRedirect('/whisky/{}/#r'.format(self.object.slug))

        elif request.POST.get('delete_cmt_id'): 
            delete_cmt_id = request.POST.get('delete_cmt_id')

            Comment.objects.filter(id=delete_cmt_id).delete()

            return HttpResponse(True)
        
        elif request.POST.get('flavor_edit') and request.POST.get('flavor_edit') == 'flavor_edit':
            ctrl_id = request.POST.get('ctrl_id')
            value = int(request.POST.get('value'))
            whisky = self.object
            user = self.request.user
            p_note = PersonalWhiskyNote.objects.filter(whisky=whisky, user=user).last()
            g_note = GeneralWhiskyNote.objects.filter(whisky=self.object).last()
            curr_num = 0

            if p_note is None:
                p_note = PersonalWhiskyNote.objects.create(
                        user = user,
                        whisky = whisky,
                    )

                if g_note is None: 
                    g_note = GeneralWhiskyNote.objects.create(
                        whisky = whisky,
                        total_notes_num = 1,
                    )

                    g_note.save()

                else:
                    curr_num = g_note.total_notes_num
                    g_note.total_notes_num+=1
                    g_note.save()
            
            g_note_return = 0

            if ctrl_id == '0':
                p_note.flora = value
                g_note_return = (g_note.flora*curr_num+value)/g_note.total_notes_num
                g_note.flora = g_note_return
            elif ctrl_id == '1':
                p_note.fruity = value
                g_note_return = (g_note.fruity*curr_num+value)/g_note.total_notes_num
                g_note.fruity = g_note_return
            elif ctrl_id == '2':
                p_note.sweet = value
                g_note_return = (g_note.sweet*curr_num+value)/g_note.total_notes_num
                g_note.sweet = g_note_return
            elif ctrl_id == '3':
                p_note.creamy = value
                g_note_return = (g_note.creamy*curr_num+value)/g_note.total_notes_num
                g_note.creamy = g_note_return
            elif ctrl_id == '4':
                p_note.nutty = value
                g_note_return = (g_note.nutty*curr_num+value)/g_note.total_notes_num
                g_note.nutty = g_note_return
            elif ctrl_id == '5':
                p_note.malty = value
                g_note_return = (g_note.malty*curr_num+value)/g_note.total_notes_num
                g_note.malty = g_note_return
            elif ctrl_id == '6':
                p_note.salty = value
                g_note_return = (g_note.salty*curr_num+value)/g_note.total_notes_num
                g_note.salty = g_note_return
            elif ctrl_id == '7':
                p_note.spicy = value
                g_note_return = (g_note.spicy*curr_num+value)/g_note.total_notes_num
                g_note.spicy = g_note_return
            elif ctrl_id == '8':
                p_note.smoky = value
                g_note_return = (g_note.smoky*curr_num+value)/g_note.total_notes_num
                g_note.smoky = g_note_return
            elif ctrl_id == '9':
                p_note.peaty = value
                g_note_return = (g_note.peaty*curr_num+value)/g_note.total_notes_num
                g_note.peaty = g_note_return
            
            p_note.save()
            g_note.save()

            return HttpResponse(g_note_return)



    def dispatch(self, request, *args, **kwargs):
        self.object = WhiskyInfo.objects.filter(slug=kwargs.get("whisky_slug")).last()

        return super(WhiskyView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(WhiskyView, self).get_context_data(*args, **kwargs)
        comments = Comment.objects.filter(whisky_id=self.object.id, publish_choice="Public").order_by('created_at')
        personal_note = PersonalWhiskyNote.objects.filter(whisky=self.object, user=self.request.user).last()
        general_note = GeneralWhiskyNote.objects.filter(whisky=self.object).last()
        if personal_note:
            personal_note_array = [personal_note.flora, personal_note.fruity, personal_note.sweet, personal_note.creamy, personal_note.nutty, personal_note.malty, personal_note.salty, personal_note.spicy, personal_note.smoky, personal_note.peaty]
        else:
            personal_note_array = [0,0,0,0,0,0,0,0,0,0]
        
        if general_note:
            general_note_array = [general_note.flora, general_note.fruity, general_note.sweet, general_note.creamy, general_note.nutty, general_note.malty, general_note.salty, general_note.spicy, general_note.smoky, general_note.peaty]
        else:
            general_note_array = [0,0,0,0,0,0,0,0,0,0]

        context.update({
            "comments": comments,
            "personal_note": personal_note,
            "general_note_array": json.dumps(list(general_note_array)),
            "personal_note_array": json.dumps(list(personal_note_array)),
        })
        context.update(distillery_list())
        return context