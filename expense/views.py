from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Entry, Profile
from django.db.models import Q
import datetime
import json



def login_page(request):
          if request.method == 'POST':
                  username = request.POST.get('username')
                  password = request.POST.get('password')

                  user = User.objects.filter(username = username)

                  user = authenticate(username = username, password = password)

                  if user:
                    login(request, user)
                    return redirect('home_page')
                  else:
                    messages.warning(request, 'Invalid credentials')
                    return redirect('login_page')

          return render(request, 'login.html')


def signup_page(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)

        if user.exists():
            messages.warning(request, "Username already exists.")
            return redirect('signup_page')

        else :
            user = User.objects.create(
                username = username,
                first_name = first_name,
            )
            user.set_password(password)
            user.save()
            profile = Profile.objects.create(
                  user = user,
                  budget = 2000,
                  expense = 0,
                  savings = 2000,
                  month = datetime.date.today().month
            )
            profile.save()
            messages.success(request, "Account created successfully")
            return redirect('signup_page')


    return render(request, 'signup.html')

@login_required(login_url="/login/")
def home_page(request):
     current_date = datetime.date.today()
     first_day_of_current_month = current_date.replace(day=1)
     entries = Entry.objects.filter(Q(user = request.user) & Q(date__gte=first_day_of_current_month)).order_by('-date')
     
#      calculating total expense 
     total_expense_of_this_month = 0
     for entry in entries:
           total_expense_of_this_month += entry.amount


     current_month = datetime.date.today().month
     current_year = datetime.date.today().year
     profile = Profile.objects.filter(Q(user = request.user) & Q(month = current_month) & Q(year=current_year))

     if not profile.exists() :
           Profile.objects.create(user= request.user, month = current_month, year = current_year, budget = 2000, expense = total_expense_of_this_month, savings = 2000-total_expense_of_this_month) 

#      budget of this month
     budget = Profile.objects.get(Q(user = request.user) & Q(month = current_month) & Q(year=current_year)).budget

#      savings of this month 
     savings = budget - total_expense_of_this_month 

#      update statistics in profile model 
     profile = Profile.objects.get(Q(user = request.user) & Q(month = current_month) & Q(year=current_year))
     profile.expense = total_expense_of_this_month
     profile.savings = savings
     profile.save()
     

     if request.method == 'GET':
           month = request.GET.get('month')
           year = request.GET.get('year')

           if month and year :
                 month = int(month)
                 year = int(year)
                 requested_date = datetime.date.today().replace(year=year, month=month, day=1)
                 
          #        retriving next_month_of_requested_date 
                 if month == 12:
                       month = 1
                       year += 1
                 else:
                       month += 1
                 next_month_of_requested_date = datetime.date.today().replace(year=year, month=month, day=1)
                 entries = Entry.objects.filter(Q(user = request.user) & Q(date__gte=requested_date) & Q(date__lt=next_month_of_requested_date)).order_by('-date')
 


     years = Profile.objects.values_list('year', flat=True).distinct().order_by('-year')
     years = list(years)

     if request.method == 'POST':
          if 'new_entry' in request.POST:
                    id = request.POST.get('id')                    
                    if id == '':
                              entry = Entry(
                              date = request.POST.get('date'),
                              description = request.POST.get('description'),
                              amount = request.POST.get('amount'),
                              user = request.user,
                              )
                              entry.save()
                              return redirect('home_page')
                    
          elif 'editForm' in request.POST:
                id = request.POST.get('editId')
                entry = Entry.objects.get(id=id)
                entry.description = request.POST.get('editDescription')
                entry.amount = request.POST.get('editAmount')
                entry.save()
                
                return redirect('home_page')
          
     context = {"entries":entries, "profile":profile, "years":years}
     
     return render(request, 'home.html', context=context)



@login_required(login_url="/login/")
def deleteEntry(request, pk):
    entry = Entry.objects.get(id=pk)
    print(entry)
    entry.delete()
    return redirect('home_page')


@login_required(login_url="/login/")
def profile_page(request):
#       user data 
      current_month = datetime.date.today().month
      current_year = datetime.date.today().year
      profile = Profile.objects.filter(Q(user = request.user) & Q(month = current_month) & Q(year=current_year))

      if not profile.exists() :
           Profile.objects.create(user= request.user, month = current_month, year = current_year, budget = 2000, expense = 0, savings = 2000) 

      profile = Profile.objects.get(Q(user = request.user) & Q(month = current_month) & Q(year=current_year))


#       some of user's recent expense
      entries = Entry.objects.filter(user = request.user).order_by('-date')
      if len(entries) > 3:
            entries = entries[:3]

      context = {"profile": profile, "entries":entries}

      if request.method == 'POST':
            if 'saveBudgetBtn' in request.POST:
                  profile.budget = request.POST.get('budget')
                  profile.save()
                  return redirect('profile_page')
            
            elif 'profileChange' in request.POST and request.user.is_authenticated:
                    # Get the first name from the POST request
                    first_name = request.POST.get('first_name')

                    # Check if first_name is not empty or None before updating
                    if first_name:
                              profile.user.first_name = first_name

                    profile.user.save()  # Save the user model
                    profile.save()  # Save the profile model, if any changes were made

                    # Redirect to the profile page after saving changes
                    return redirect('profile_page')

      return render(request, 'profile.html', context=context)



@login_required(login_url="/login/")
def analysis_page(request):
      years = Profile.objects.filter(user = request.user).values_list('year', flat=True).distinct().order_by('-year')

      years = list(years)
      print(years)

      profiles = Profile.objects.filter(user = request.user).values('budget', 'savings', 'year', 'month', 'expense').order_by('month')

      profiles = list(profiles)

      profiles = (json.dumps(profiles))

      context = { "years":years, "profiles":profiles}

      return render(request, 'analysis.html', context=context)



def logout_page(request):
      logout(request)
      return redirect('login_page')