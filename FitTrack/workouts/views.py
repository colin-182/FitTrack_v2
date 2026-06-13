from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WorkoutPlan, WorkoutLog, Category
from .forms import WorkoutPlanForm, WorkoutLogForm

@login_required
def dashboard(request):
    plans = WorkoutPlan.objects.filter(assigned_to=request.user)
    logs = WorkoutLog.objects.filter(user=request.user).order_by('-date')[:5]
    return render(request, 'workouts/dashboard.html', {'plans': plans, 'logs': logs})

@login_required
def plan_list(request):
    plans = WorkoutPlan.objects.filter(assigned_to=request.user)
    return render(request, 'workouts/plan_detail.html', {'plans': plans})

@login_required
def plan_detail(request, pk):
    plan = get_object_or_404(WorkoutPlan, pk=pk)
    return render(request, 'workouts/plan_detail.html', {'plan': plan})

@login_required
def plan_create(requset):
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            plan = form.save(comit=False)
            plan.created_by = request.user
            plan.assigned_to = request.user
            plan.save()
            messages.success(request, 'Workout plan created!')
            return redirect('plan_list')
        else:
            form = WorkoutPlanForm()
        return render(request, 'workouts/plan_form.html', {'form': form, 'title': 'Create Plan'})
    
    @login_required
    def plan_edit(request, pk):
        plan = get_object_or_404(WorkoutPlan, pk=pk)
        if request.method == 'POST':
            form = WorkoutPlanForm(request.POST, instance=plan)
            if form.is_valid():
                form.save()
                messages.success(request, 'Workout plan updated!')
                return redirect('plan_list')
            else:
                form = WorkoutPlanForm(instance=plan)
            return render(request, 'workouts/plan_form.html', {'form': form, 'title': 'Edit Plan'})
        
    @login_required
def plan_delete(request, pk):
    plan = get_object_or_404(WorkoutPlan, pk=pk)
    if request.method == 'POST':
        plan.delete()
        messages.success(request, 'Workout plan deleted!')
        return redirect('plan_list')
    return render(request, 'workouts/plan_confirm_delete.html', {'plan': plan})

@login_required
def log_create(request):
    if request.method == 'POST':
        form = WorkoutLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            messages.success(request, 'Workout logged!')
            return redirect('log_history')
    else:
        form = WorkoutLogForm()
    return render(request, 'workouts/log_form.html', {'form': form})

@login_required
def log_history(request):
    logs = WorkoutLog.objects.filter(user=request.user).order_by('-date')
    return render(request, 'workouts/log_history.html', {'logs': logs})