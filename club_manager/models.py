from django.db import models
from django.contrib.auth.models import User


# models for club_manager
class Club(models.Model):
    club_name = models.CharField(max_length=100)
    club_type = models.CharField(max_length=50, default="Chess")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.club_name


class Member(models.Model):
    """
    Members represent all people associated with a club: players, coaches, parents, etc.
    """
    # Members belong to a specific club
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birthdate = models.DateField('birth date')
    email = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Group(models.Model):
    # groups belong to a specific club
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.group_name}"


class Coach(models.Model):
    # Coach is a member
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    # Coaches are associated with one particular group
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "coaches"

    def __str__(self):
        return f"Coach: {self.member.name}"


class Officer(models.Model):
    # Officer is a member
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    # Officers serve for a given club
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    # Officers have a role such as president, treasurer, etc.
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.member.name}, {self.role}"


class Player(models.Model):
    # players are members
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    # players belong to a group
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # skill level can be indicated (beginner, intermediate, etc)
    ability_level = models.CharField(max_length=20, default="Beginner")

    def __str__(self):
        return f"{self.member.name}, {self.ability_level}, {self.member.email}"


class Tournament(models.Model):
    # tournaments are associated with a specific club
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    tourn_name = models.CharField(max_length=200, default="Tournament")
    # tournaments have players
    players_list = models.ManyToManyField(Player)
    # tournaments have a primary tournament director
    t_date = models.DateTimeField("tournament date")

    def __str__(self):
        return f"{self.tourn_name}, Date: {self.t_date}"
