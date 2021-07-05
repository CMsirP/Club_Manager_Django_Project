from django.db import models


# models for club_manager
class Member(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField('birth date')
    email = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Officer(models.Model):
    officer = models.OneToOneField(Member, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    date_elected = models.DateField("date elected")

    def __str__(self):
        return f"{self.officer.name}, {self.role}"


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
        return f"{self.club_name}, President: {self.president.officer.name}"


class Coach(models.Model):
    coach = models.ForeignKey(Member, on_delete=models.CASCADE)
    yrs_experience = models.IntegerField()

    def __str__(self):
        return f"Coach: {self.coach.name}"


class Group(models.Model):
    # groups belong to a specific club
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)
    primary_coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True)

    def get_players(self):
        return Group.objects.get(Player)

    def __str__(self):
        return f"Group: {self.group_name}, Coached by: {self.primary_coach}"


class Player(models.Model):
    # players are members
    player = models.OneToOneField(Member, on_delete=models.CASCADE)
    # players usually belong to a group
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True)
    # skill level can be indicated (beginner, intermediate, etc)
    ability_level = models.CharField(max_length=20, default="Beginner")

    def __str__(self):
        return f"{self.player.name}, {self.ability_level}"


class Tournament(models.Model):
    tourn_name = models.CharField(max_length=200, default="Tournament")
    # tournaments have players
    players_list = models.ManyToManyField(Player)
    # tournaments have a primary tournament director
    primary_t_director = models.ForeignKey(Member, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    t_date = models.DateTimeField("tournament date")

    def __str__(self):
        return f"{self.tourn_name}, Director: {self.primary_t_director}, " \
               f"Date: {self.t_date}"
