# Import necessary Django modules and libraries
from django.shortcuts import render, get_object_or_404, redirect  # For rendering templates, fetching objects, and redirecting
from rest_framework import viewsets  # For creating REST API viewsets
from .models import Todo  # Import the Todo model from the current app
from .serializers import TodoSerializer  # Import the TodoSerializer for REST API
# from .forms import TodoForm  # Import the TodoForm (currently commented out)

# View to display a list of all Todo items
def todo_list(request):
    # Fetch all Todo objects from the database
    todos = Todo.objects.all()
    # Render the 'todoapp/home.html' template, passing the todos as context
    return render(request, 'todoapp/home.html', {'todos': todos})

# View to display details of a specific Todo item
def todo_detail(request, pk):
    # Fetch the Todo object with the given primary key (pk), or return a 404 error if not found
    todo = get_object_or_404(Todo, pk=pk)
    # Redirect to the root URL ("/") - This is likely a placeholder and should be fixed
    return httpsresponse("/")

# View to create a new Todo item
def todo_create(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = TodoForm(request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # Save the form data to the database and get the saved Todo object
            todo = form.save()
            # Redirect to the detail view of the newly created Todo item
            return redirect('todo_detail', pk=todo.pk)
    else:
        # If the request method is not POST, create an empty form
        form = TodoForm()
    # Render the 'todoapp/todo_form.html' template, passing the form as context
    return render(request, 'todoapp/todo_form.html', {'form': form})

# View to update an existing Todo item
def todo_update(request, pk):
    # Fetch the Todo object with the given primary key (pk), or return a 404 error if not found
    todo = get_object_or_404(Todo, pk=pk)
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted data and the existing Todo object
        form = TodoForm(request.POST, instance=todo)
        # Check if the form data is valid
        if form.is_valid():
            # Save the updated form data to the database
            todo = form.save()
            # Redirect to the detail view of the updated Todo item
            return redirect('todo_detail', pk=todo.pk)
    else:
        # If the request method is not POST, create a form with the existing Todo object
        form = TodoForm(instance=todo)
    # Render the 'todoapp/todo_form.html' template, passing the form as context
    return render(request, 'todoapp/todo_form.html', {'form': form})

# View to delete a Todo item
def todo_delete(request, pk):
    # Fetch the Todo object with the given primary key (pk), or return a 404 error if not found
    todo = get_object_or_404(Todo, pk=pk)
    # Check if the request method is POST (confirmation of deletion)
    if request.method == 'POST':
        # Delete the Todo object from the database
        todo.delete()
        # Redirect to the list view after deletion
        return redirect('todo_list')
    # Render the 'todoapp/todo_confirm_delete.html' template, passing the Todo object as context
    return render(request, 'todoapp/todo_confirm_delete.html', {'todo': todo})

# Django REST Framework ViewSet for the Todo model
class TodoviewSet(viewsets.ModelViewSet):
    # Define the queryset to fetch all Todo objects
    queryset = Todo.objects.all()
    # Specify the serializer class to use for the Todo model
    serializer_class = TodoSerializer