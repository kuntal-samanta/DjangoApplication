from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
from .models import *
import secrets
import string
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def Big_Number_Generator():
    letters = string.ascii_letters + string.digits + string.hexdigits
    l = [secrets.choice(letters) for i in range(20)]
    num = ''
    for i in l:
        num = num + i
    return num


def Home(request):
    try:
        user_id = request.session['user_id']
        u = User.objects.get(id=user_id)
        ud = UserDetails.objects.get(user_id=user_id)
        post = Post.objects.all().order_by('-create_at')
        tag = Tags.objects.all().order_by('-create_at')
        hightlight = post[:5]
        
        paginator = Paginator(post, 10)
        try:
            page = request.GET.get('page', 1)
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)
        
        return render(request, 'UserApp/home.html', context={'post': post, 'ud': ud, 'u': u, 'tag': tag, 'hightlight': hightlight, 'post_list': post_list})
    except Exception as e:
        return redirect('/login/')


def ViewPost(request, slug):
    try:
        request.session['user_id']
        post_id = slug
        post = Post.objects.get(id=post_id)
        
        user_email = post.created_by.email
        ud = UserDetails.objects.get(user__email=user_email)
        
        return render(request, 'UserApp/post.html', context={'post': post, 'ud': ud})
    except Exception as e:
        print("#"*50, e)
        return redirect('/login/')


def CreateBlog(request):
    try:
        user_id = request.session['user_id']
        if request.method == 'GET':
            tag = Tags.objects.all().order_by('-create_at')
            return render(request, 'UserApp/create-post.html', context={'tag': tag})
        else:
            image = request.FILES['imgfile']
            heading = request.POST['headername']
            body = request.POST['message']
            tag = request.POST['tag_name']
            u = User.objects.get(id=user_id)
            
            p = Post(
                image=image,
                heading=heading,
                body=body,
                tag=tag,
                created_by=u
            )
            p.save()
            return redirect('/')
    except Exception as e:
        return redirect('/login/')


def SignUp(request):
    try:
        request.session['user_id']
        return redirect('/')
    except Exception as e:
        if request.method == 'GET':
            return render(request, 'UserApp/signup.html', context={})
        else:
            try:
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                birthday = request.POST['birthday']
                gender = request.POST['gender']
                email = request.POST['email']
                password = request.POST['password']
                phone = request.POST['phone']
                pImg = request.FILES['pImg']
                
                # Data format changed to 2000-11-04
                dd = birthday.split('/')[0]
                mm = birthday.split('/')[1]
                yyyy = birthday.split('/')[2]
                birthday = str(yyyy+ "-" + mm + '-' + dd)
                
                u = User(
                    username=email.split('@')[0],
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    date_joined=datetime.datetime.now(),
                )
                u.save()
                u.set_password(password)
                u.save()
                
                ud = UserDetails(
                    user=u,
                    dob=birthday,
                    gender=gender,
                    phone=phone,
                    profile_photo=pImg
                )
                ud.save()
        
                return redirect('/login/')
            
            except Exception as e:
                try:
                    u = User.objects.get(email=email).delete()
                except:
                    pass
                return redirect('/signup/')
        

def Login(request):
    try:
        request.session['user_id']
        return redirect('/')
    except Exception as e:
        if request.method == 'GET':
            return render(request, 'UserApp/login.html', context={})
        else:
            email = request.POST['email']
            password = request.POST['password']
            
            print("$"*30)
            
            try:
                u = User.objects.get(email=email)
                if check_password(password, u.password):
                    request.session['user_id'] = u.id
                    return redirect('/')
                else:
                    return redirect('/login/')
            except Exception as e:
                print("#"*30, e)
                return redirect('/login/')



def CheckEmailId(request):
    pass

def CheckUserName(request):
    pass

def Logout(request):
    try:
        del request.session['user_id']
        return redirect('/login/')
    except:
        return redirect('/login/')
'''
try:
        usrmail = request.GET.get('mail')
        UserObj = UserDetails.objects.get(usrMail=usrmail)
        if usrmail == UserObj.usrMail:
            is_taken = True
        else:
            is_taken = False
    except Exception as e:
        print("Api calling issue Email Check: ", e)
        is_taken = False
    
    context = {'is_taken': is_taken}
    return JsonResponse(context)
'''

