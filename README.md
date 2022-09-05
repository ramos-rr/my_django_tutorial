# MY WEBSITE

Implementing a Django Website with Django Documentation<br>

## TUTORIAL

### First Steps
- [PART 1 - REQUEST AND RESPONSES](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)<br>
<br>
- [PART 2 = MODELS AND DE ADMIN SITE](https://docs.djangoproject.com/en/4.1/intro/tutorial02/)<br>
<br>
- [PART 3 - VIEWS AND TEMPLATES](https://docs.djangoproject.com/en/4.1/intro/tutorial03/)<br>
<br>
- [PART 4 - FORMS AND GENERIC VIEWS](https://docs.djangoproject.com/en/4.1/intro/tutorial04/)<br>
<br>
- [PART 5 - TESTING](https://docs.djangoproject.com/en/4.1/intro/tutorial05/)<br>
<br>
- [PART 6 - STATIC FILES](https://docs.djangoproject.com/en/4.1/intro/tutorial06/)<br>
<br>
- [PART 7 - CUSTOMIZNG THE ADMIN SITE](https://docs.djangoproject.com/en/4.1/intro/tutorial07/)<br>
<br>
## TIPS: create a question and a choice commands<br>
##### Create a Question
- Run: `python manage.py shell` to activate django terminal;<br>
- Run: `>>> from from polls.models import Choice, Question`;<br>
- Run: `>>> from from django.utils import timezone`;<br>
- Create a question: `>>> q = Question.objects.create(question_text='..text..', pub_date=timezone.now()`
- Get ID: `>>> q.id`;<br>
- Filter by int: `>>> Question.objects.filter(id=4)` or `>>> Question.objects.get(pk=4)`;<br>
- Filter by str: `>>> Question.objects.filter(question_text__startswith="Is it")`;<br>
- Filter by date (past): `>>> Question.objects.filter(pub_date__lte=timezone.now())`;<br>
##### Manage Choices for this question
- See all Choices: `>>> q.choice_set.all()`;<br>
- Create Choice for question: `>>> q.choice_set.create(choice_text='..text..', votes=0`;<br>
- See how many choice is there: `>>> q.choice_set.count()`;<br>
- Set choice as variable: `>>> c = q.choice_set.filter(choice_text='..text..')`
- Delete choice: `>>> c.delete()`
