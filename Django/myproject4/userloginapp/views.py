from django.shortcuts import redirect, render

users = [
    {
        'id': 1,
        'email': 'user1@gmail.com',
        'password': 'user1@123'
    },
    {
        'id': 2,
        'email': 'user2@gmail.com',
        'password': 'user2@123'
    },
    {
        'id': 3,
        'email': 'user3@gmail.com',
        'password': 'user3@123'
    }
]

# Create your views here.

def home(request):
    user_id = request.GET.get('user_id')

    if user_id:
        user = ''
        for u in users:
            if str(u['id']) == user_id:
                user = u
                break
        return render(request, 'userloginapp/home.html', {'user': user})

    return redirect('/login')

def login(request):
    errorMsg = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        for user in users:
            if user['email'] == email and user['password'] == password:
                return redirect(f"/home?user_id={user['id']}")
        else:
            errorMsg = 'Invalid Credentials. Please try again.'
        
    return render(request, 'userloginapp/login.html' , {'error': errorMsg})