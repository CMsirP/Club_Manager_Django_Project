from django.db import models


# models for club_manager
class Member(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateTimeField('birth date')
    email = models.CharField(max_length=200)
    phone = models.IntegerField()


class Officer(models.Model):
    officer = models.OneToOneField(Member, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    date_elected = models.DateTimeField("date elected")


class Location(models.Model):
    loc_name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()

    def __str__(self):
        return f"{self.loc_name}, {self.city}, {self.state}"


class Club(models.Model):
    club_name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # club must have at least one officer as president
    president = models.ForeignKey(Officer, on_delete=models.CASCADE)

    def __str__(self):
        return self.club_name


class Coach(models.Model):
    coach = models.ForeignKey(Member, on_delete=models.CASCADE)
    yrs_experience = models.IntegerField()


class Group(models.Model):
    # groups belong to a specific club
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)
    primary_coach = models.ForeignKey(Coach, on_delete=models.CASCADE)


class Player(models.Model):
    player = models.ForeignKey(Member, on_delete=models.CASCADE)
    # players belong to a group
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Tournament(models.Model):
    players_list = models.ManyToManyField(Player)
    primary_t_director = models.ForeignKey(Member, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    date = models.DateTimeField("tournament date")
