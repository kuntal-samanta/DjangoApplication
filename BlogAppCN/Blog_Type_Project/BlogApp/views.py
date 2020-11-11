from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
from .models import UserDetails, Blog
import secrets
import string


def Big_Number_Generator():
    letters = string.ascii_letters + string.digits + string.hexdigits
    l = [secrets.choice(letters) for i in range(20)]
    num = ''
    for i in l:
        num = num + i
    return num


def Home(req):
    try:
        usrmail = req.session['usrmail']
        try:
            loggedInuserPost = Blog.objects.all().filter(blogCreatorMail=usrmail)[:5]
        except:
            loggedInuserPost = ''
        BlogObj = Blog.objects.all()
        context = {'loggedin': True, 'usrmail': usrmail, 'BlogObj': BlogObj, \
            'loggedInuserPost': loggedInuserPost}

    except Exception as e:
        print("Home", e)
        context = {'loggedin': False}
    
    return render(req, 'BlogApp/home.html', context=context)


def CreateBlog(req):
    try:
        usrmail = req.session['usrmail']
        if req.method == 'POST':
            UserObj = UserDetails.objects.get(usrMail=usrmail)
            # Blog DataSet
            blogId = Big_Number_Generator()
            blogHeading = req.POST['headername']
            blogContent = req.POST['message']
            blogImage = req.FILES['imgfile']
            blogCreatorName = UserObj.usrFirstName + " " + UserObj.usrLastName
            blogCreatorMail = UserObj.usrMail
            blogCreatorImage =  UserObj.usrImage
            blogLikedBy = []
            blogDisLikeBy = []
            blogComment = []
            blogLikeCount = 0
            blogDisLikeCount = 0
            blogPostTime = datetime.datetime.now()

            try:
                blogObj = Blog(blogId=blogId,blogHeading=blogHeading,blogContent=blogContent,\
                            blogImage=blogImage,blogCreatorName=blogCreatorName,blogCreatorMail=blogCreatorMail,\
                            blogCreatorImage=blogCreatorImage,blogLikedBy=blogLikedBy,blogDisLikeBy=blogDisLikeBy,\
                            blogComment=blogComment,blogLikeCount=blogLikeCount,blogDisLikeCount=blogDisLikeCount,\
                            blogPostTime=blogPostTime)
                blogObj.save()
            except Exception as e:
                print("Blog Post Error : ", e)
            return redirect('/')
        else:
            return render(req, 'BlogApp/postblog.html', context={})

    except Exception as e:
        print("Blog Create Error : ", e)
        response = redirect('/login')
        return response


def SignUp(req):
    try:
        usrmail = req.session['usrmail']
        response = redirect('/')
        return response
    except Exception as e:
        print("SignUp", e)
        if req.method == 'POST':
            first_name = req.POST['firstName']
            last_name = req.POST['lastName']
            blogusername = req.POST['bloguser']
            blogusrmail = req.POST['e_mail']
            userImg = req.FILES['bloguserImg1']
            password = req.POST['psw']
            usrId = Big_Number_Generator()
            today = datetime.datetime.now()
            
            try:
                NewObj = UserDetails(usrId=usrId,usrName=blogusername,usrFirstName=first_name,
                                    usrLastName=last_name,usrMail=blogusrmail,usrImage=userImg,\
                                    usrPassword=password, usrCreated=today)
                NewObj.save()
                response = redirect('/login')
                return response
            
            except Exception as e:
                print("Data Save : ", e)
                response = redirect('/signup')
                return response

        else:
            context = {}
            return render(req, 'BlogApp/signup.html', context=context)


def Login(req):
    try:
        usrmail = req.session['usrmail']
        response = redirect('/')
        return response
    except Exception as e:
        print("Login", e)
        if req.method == 'POST':
            blogusername = req.POST['bloguser']
            user_psw = req.POST['pswd']
            UserObj = UserDetails.objects.get(usrName=blogusername)
            if UserObj.usrName == blogusername:
                if UserObj.usrPassword == user_psw:
                    req.session['usrmail'] = UserObj.usrMail
                    return CreateBlog(req)
            
            response = redirect('/login')
            return response
        else:
            context = {}
            return render(req, 'BlogApp/login.html', context=context)


def CheckEmailId(req):
    try:
        usrmail = req.GET.get('mail')
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


def CheckUserName(req):
    try:
        usrnm = req.GET.get('usrname')
        UserObj = UserDetails.objects.get(usrName=usrnm)
        if usrnm == UserObj.usrName:
            is_taken = True
        else:
            is_taken = False
    except Exception as e:
        print("Api calling issue usrname ", e)
        is_taken = False
    
    context = {'is_taken': is_taken}
    return JsonResponse(context)


def LikePost(req):
    try:
        usrmail = req.session['usrmail']
        postid = req.GET.get('wholike')
        blogObj = Blog.objects.get(blogId=postid)
        if usrmail in blogObj.blogLikedBy:
            blogObj.blogLikedBy.remove(usrmail)
            blogObj.save()
        else:
            blogObj.blogLikedBy.append(usrmail)
            blogObj.save()
        success = True
    except Exception as e:
        print("Like Post : ", e)
        success = False

    context = {'success': success}
    return JsonResponse(context)


def DisLikePost(req):
    try:
        usrmail = req.session['usrmail']
        postid = req.GET.get('whodislike')
        blogObj = Blog.objects.get(blogId=postid)
        if usrmail in blogObj.blogDisLikeBy:
            blogObj.blogDisLikeBy.remove(usrmail)
            blogObj.save()
        else:
            blogObj.blogDisLikeBy.append(usrmail)
            blogObj.save()
        success = True
    except Exception as e:
        print("")
        success = False

    context = {'success': success}
    return JsonResponse(context)


def MakeComment(req):
    try:
        usrmail = req.session['usrmail']
        postid = req.GET.get('postid')
        comment = req.GET.get('comment')
        blogObj = Blog.objects.get(blogId=postid)
        blogObj.blogComment.append(comment)
        blogObj.save()
        success = True
    except Exception as e:
        print("Logged Out User : ", e)
        success = False
    context = {'success': success}
    return JsonResponse(context)


def Logout(req):
    try:
        del req.session['usrmail']
        return redirect('/login')
    except:
        return redirect('/login')