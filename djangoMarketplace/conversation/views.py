from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from item.models import Item

from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
        'title': 'Inbox'
    })

@login_required
def detail(request, pk):
    # Get conversation
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    # Mark all messages as read
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
        'title': 'Conversation'
    })

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        pass
        #return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # Create conversation
            conversation = Conversation.objects.create(item=item)
            # Add members: item creator and current user
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            # Create conversation message
            conversation_message = form.save(commit=False)
            # Set the conversation to the conversation we just created
            conversation_message.conversation = conversation
            # Set the message creator to the current user
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form,
        'title': 'New Conversation',
    })