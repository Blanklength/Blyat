from django.db import models



class Geratekategorie(models.Model):
    class Meta:
        verbose_name = 'Gerätekategorie'
        verbose_name_plural = 'Gerätekategorien'

    name = models.CharField(verbose_name='Name', max_length=30, unique=True)
    description = models.TextField(verbose_name='Beschreibung', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name




class Trakt(models.Model):
    class Meta:
        verbose_name = 'Trakt'
        verbose_name_plural = 'Trakte'

    name = models.CharField(verbose_name='Name', max_length=30, unique=True)
    description = models.TextField(verbose_name='Beschreibung', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name



class Stockwerk(models.Model):
    class Meta:
        verbose_name = 'Stockwerk'
        verbose_name_plural = 'Stockwerke'

    name = models.CharField(verbose_name='Name', max_length=30, unique=True)
    description = models.TextField(verbose_name='Beschreibung', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Geratehersteller(models.Model):
    class Meta:
        verbose_name = 'Gerätehersteller'
        verbose_name_plural = 'Gerätehersteller'

    name = models.CharField(verbose_name='Name', max_length=30, unique=True)
    description = models.TextField(verbose_name='Beschreibung', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name





class Raum(models.Model):
    class Meta:
        verbose_name = 'Raum'
        verbose_name_plural = 'Räume'

    name = models.CharField(verbose_name='Name', max_length=30, unique=True)
    building_section = models.ForeignKey(Trakt, verbose_name='Bauabschnitt', on_delete=models.PROTECT, default=None)
    floor = models.ForeignKey(Stockwerk, verbose_name='Etage', on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.name


class Gerat(models.Model):
    class Meta:
        verbose_name = 'Gerät'
        verbose_name_plural = 'Geräte'

    class Statusptionen(models.IntegerChoices):
        LIMITED_FUNCTIONALITY = 1, 'beschränkt funktionsfähig'
        FULLY_FUNCTIONAL = 5, 'funktionsfähig'
        NOT_FUNCTIONAL = 0, 'funktionsunfähig'

    name = models.CharField(
        verbose_name='Name',
        max_length=40
    )
    kosten = models.DecimalField(verbose_name='Kosten', max_digits=8, decimal_places=2, null=True, blank=True)
    gerate_hersteller = models.ForeignKey(
        Geratehersteller,
        verbose_name='Hersteller',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.IntegerField(
        verbose_name='Status',
        choices=Statusptionen.choices,
        null=True, blank=True
    )
    description = models.TextField(verbose_name='Beschreibung', max_length=500, null=True, blank=True)
    bestellungs_datum = models.DateField(verbose_name='Bestellungsdatum', null=True, blank=True)
    serien_nummer = models.CharField(verbose_name='Seriennummer', max_length=40, null=True, blank=True)
    garantie_monate = models.IntegerField(
        verbose_name='Garantie (Monate)',
        choices=[(i, i) for i in range(1, 12)],
        null=True,
        blank=True)
    garantie_jahre = models.IntegerField(
        verbose_name='Garantie (Jahre)',
        choices=[(i, i) for i in range(1, 20)],
        null=True,
        blank=True)
    gerate_kategorie = models.ForeignKey(Geratekategorie, verbose_name='Kategorie', on_delete=models.CASCADE,
                                         default=None)
    raum = models.ForeignKey(
        Raum,
        verbose_name='Raum',
        on_delete=models.CASCADE,
        default=None
    )

    def __str__(self):
        return self.name

class Ticket(models.Model):
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    class StatusOptions(models.IntegerChoices):
        OPEN = 1, 'Offen'
        CLOSED = 0, 'Erledigt'

    gerat = models.ForeignKey(Gerat, verbose_name='Gerät', on_delete=models.CASCADE, default=None)
    titel = models.CharField(verbose_name='Titel', max_length=40)
    description = models.TextField(verbose_name='Beschreibung', max_length=500)
    status = models.IntegerField(verbose_name='Status', choices=StatusOptions.choices)
    erstellungs_datum = models.DateTimeField(verbose_name='Erstellungsdatum', auto_now_add=True)

    def __str__(self):
        return self.titel