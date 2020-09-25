from tkinter import Canvas, CENTER


class Jeton:
    """
    Cette classe représente un jeton.
    Les attributs d'un jeton sont:
    - lettre: str, représentant la lettre écrite sur le jeton. Par convention toutes les lettres au scrabble sont en
    majuscules. Dans ce travail nous ne considérons pas les jetons jokers qui n'ont aucune lettre inscrite.
    - valeur: int, compris entre 0 et 20 inclusivement et représentant le nombre de points associé au jeton.
    """

    def __init__(self, lettre, valeur):
        """
        Constructeur de la classe. Permet de créer un Jeton à partir d'une lettre et d'un nombre de points
        :param lettre: str, représentant la lettre écrite sur le jeton.
        :param valeur: int, > 0 représentant le nombre de points associé au jeton.
        :exception: Levez une exception avec assert si la valeur ne respecte pas
        la condition suivante 0 <= valeur <= 20 ou si la lettre n'est pas en majuscule.
        """
        assert 0 <= valeur <= 20, "La valeur doit être inclue entre 0 et 20 inclusivement"
        assert lettre.isupper(), "La lettre doit être en majuscule"

        self.lettre = lettre
        self.valeur = valeur

    def __repr__(self):
        """ *** Vous n'avez pas à coder cette méthode ***
        Formatage d'un jeton. Cette méthode est appelée lorsque vous faites str(v) où v est un jeton.
        :return: str, correspondant au formatage du jeton.
        """
        if self is None:
            res = ""
        else:
            if self.valeur < 10:
                res = "{}{}".format(self.lettre, chr(0x2080 + self.valeur))
            else:
                res = "{}{}{}".format(self.lettre, chr(0x2080 + int(self.valeur/10)),
                                      chr(0x2080 + int(self.valeur % 10)))
        return res


class Case:
    """
    Cette classe représente une case sur un tableau de scrabble.

    Les attributs d'une case sont:
    - multiplicateur: int, >= 1 et <= 3.
                        Si la case n'est pas spéciale son multiplicateur de points est de 1.
                        Autrement, il sera de 2 dans le cas d'une case compte double ou
                        3 dans le cas d'une case compte triple.
    - type: str, 'M' si la case est spéciale et affecte le pointage des mots;
                 'L' si la case est spéciale et affecte le pointage des lettres;
                 None si la case n'est pas spéciale.
    - jeton_occupant: Jeton,
    """

    def __init__(self, multiplicateur=1, type=None):
        """
        Constructeur de la classe.
        Notez qu'une case nouvellement créée est vide, c'est-à-dire le jeton occupant est None.
        :param multiplicateur: (int, optionel) multiplicateur de la case.
        :param type: (str, optionel) type de la case.
        :exception: Levez une exception avec assert si le multiplicateur ne respecte pas
        la condition suivante 1 <= multiplicateur <= 3 ou si le type n'est ni None, ni 'M', ni 'L'.
        """
        assert 1 <= multiplicateur <= 3, "Le multiplicateur doit être inclu entre 1 et 3 inclusivement"
        assert type in [None, "M", "L"], "Le type est invalide"

        self.multiplicateur = multiplicateur
        self.type = type
        self.jeton_occupant = None

    def est_vide(self):
        """
        Vérifie si une case est vide ou pas (jeton_occupant est None ou pas).
        :return: True si la case est vide, False sinon.
        """
        return self.jeton_occupant is None

    def placer_jeton(self, jeton):
        """
        Place un jeton dans la case.
        :param jeton: Jeton, objet à placer dans la case.
        :return: Ne retourne rien.
        :exception: Levez une exception avec assert si la case est déjà occupée.
        """
        assert Case.est_vide(self), "La case est déjà occupée"
        self.jeton_occupant = jeton

    def retirer_jeton(self):
        """
        Retire le jeton de la case.
        :return: Le jeton retiré.
        :exception: Levez une exception avec assert si la case est vide.
        """
        jeton = self.jeton_occupant
        self.jeton_occupant = None
        return jeton

    def valeur_jeton(self):
        """
        Permet de trouver la valeur du jeton dans la case.
        :return: int, valeur du jeton occupant.
        :exception: Levez une exception avec assert si la case est vide.
        """
        assert not Case.est_vide(self), "La case est vide"
        return self.jeton_occupant.valeur

    def lettre_jeton(self):
        """
        Permet de trouver la lettre inscrite sur le jeton dans la case.
        :return: str, lettre du jeton occupant.
        :exception: Levez une exception avec assert si la case est vide.
        """
        return self.jeton_occupant.lettre
    
    @property
    def code_couleur(self):
        """  *** Vous n'avez pas à coder cette méthode ***
        Méthode permettant de trouver la couleur associée à une case.
        :return: int, code de couleur de la case.
        """
        if self.type == "M" and self.multiplicateur == 2:
            return 43
        elif self.type == "M" and self.multiplicateur == 3:
            return 41
        elif self.type == "L" and self.multiplicateur == 2:
            return 46
        elif self.type == "L" and self.multiplicateur == 3:
            return 44
        else:
            return 0

    def __str__(self):

        """  *** Vous n'avez pas à coder cette méthode ***
        Formatage d'une case. Cette méthode est appelée lorsque vous faites str(v) où v est un case
        :return: str, correspondant au formatage de la case.
        """
        s = "" if self.est_vide() else str(self.jeton_occupant)
        return "\x1b[0;30;{}m{:^4s}\x1b[0m".format(self.code_couleur, s)


class Chevalet(Canvas):

    DIMENSION = 7
    PIXELS_PAR_CASE = 45
    FONT_SIZE = PIXELS_PAR_CASE // 6
    COULEUR_BORDURE = "white"

    def __init__(self, parent, longueur=PIXELS_PAR_CASE, largeur=DIMENSION * PIXELS_PAR_CASE):
        """
        Constructeur d'un chevalet.

        """
        super().__init__(parent, height=longueur, width=largeur)
        self.couleur = "#e5cca4"

        self.cases = [Case() for _ in range(Chevalet.DIMENSION)]

        for i in range(Chevalet.DIMENSION):

                x1 = i * Chevalet.PIXELS_PAR_CASE
                y1 = 0
                x2 = x1 + Plateau.PIXELS_PAR_CASE
                y2 = y1 + Plateau.PIXELS_PAR_CASE
                self.create_rectangle(x1, y1, x2, y2, fill=self.couleur, outline=Plateau.COULEUR_BORDURE, tags='case')

    def dessiner_jeton_chevalet(self, jeton, pos, position_selectionnee=None, nb_pixels_per_case=PIXELS_PAR_CASE):
        d = nb_pixels_per_case//2
        debut_ligne = pos * nb_pixels_per_case
        debut_colonne, fin_ligne, fin_colonne = 0, debut_ligne + nb_pixels_per_case, nb_pixels_per_case
        if pos == position_selectionnee:
            if jeton is None or jeton == "":
                self.create_rectangle(debut_ligne, debut_colonne, fin_ligne, fin_colonne,  fill='#00a8f3')
            else:
                self.create_rectangle(debut_ligne, debut_colonne, fin_ligne, fin_colonne, fill='#00a8f3')
                self.create_text((debut_ligne + d, debut_colonne + d),
                                 font=('Times', '{}'.format(int(nb_pixels_per_case*.5))), text=str(jeton))
        else:
            if jeton is None or jeton == "":
                self.create_rectangle(debut_ligne, debut_colonne, fin_ligne, fin_colonne, fill='#e5cca4')
            else:
                self.create_rectangle(debut_ligne, debut_colonne, fin_ligne, fin_colonne, fill='#b9936c')
                self.create_text((debut_ligne + d, debut_colonne + d),
                                 font=('Times', '{}'.format(int(nb_pixels_per_case*.5))), text=str(jeton))


class Plateau(Canvas):
    """
    Cette classe représente un plateau de scrabble.
    Une partie de la logique du jeu sera implémentée ici donc lisez bien les spécifications de chaque méthode.
    ex:
             1    2    3    4    5    6    7    8    9   10   11   12   13   14   15
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        A |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | A
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        B |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | B
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        C |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | C
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        D |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | D
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        E |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | E
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        F |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | F
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        G |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | G
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        H |    |    |    |    |    |    |    | ★  |    |    |    |    |    |    |    | H
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        I |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | I
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        J |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | J
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        K |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | K
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        L |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | L
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        M |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | M
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        N |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | N
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        O |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | O
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
             1    2    3    4    5    6    7    8    9   10   11   12   13   14   15

    Nous avons un attribut de classe:
    - DIMENSION qui représente la dimension (nombre de lignes ou de colonnes) pour le plateu de scrabble. Par défaut sa
    valeur est de 15.

    Un plateau de scrabble a pour attribut:
    - cases: Case list list, une liste de liste de cases.
            Le programmeur peut avoir accès et manipuler les cases du plateau avec des indexes i et j, tels que 0 <= i <
            Plateau.DIMENSION et 0 <= j < Plateau.DIMENSION.
            Pour vous aider un peu:
                * cases[i] vous retourne la i+1 ème ligne du plateau.
                (L'index i == 0 correspond donc à la première ligne,
                et ainsi de suite).
                * cases[i][j] vous donne la case au croisement de la i+1 ème ligne et de la j+1 ème colonne du plateau.
                (L'index j == 0 correspond donc à la première colonne, et ainsi de suite).

            L'utilisateur de la classe, désignera les cases grâce à un code au format « XY » où X représente une lettre
            comprise entre 'A' et 'O', et Y un nombre compris entre 1 et 15. Ex: K9, E15.
            - La lettre désigne une ligne: 'A' pour la 1ère ligne, B pour la seconde ligne, etc.
            - Le nombre désigne une colonne: 5 correspond à la 5ème colonne.
            Par exemple:
            - K9 permet de désigner la case à l'intersection de la 11ème ligne et de la 9ème colonne.
            - E15 permet de désigner la case à l'intersection de la 5ème ligne et 15ème colonne.
            Note: Vous pouvez vour servir du graphe ASCII plus haut pour une meilleure compréhension.
    """

    DIMENSION = 15
    PIXELS_PAR_CASE = 45
    FONT_SIZE = PIXELS_PAR_CASE // 6
    COULEUR_BORDURE = "white"

    def __init__(self, parent, longueur=DIMENSION * PIXELS_PAR_CASE, largeur=DIMENSION * PIXELS_PAR_CASE):
        """ *** Vous n'avez pas à coder cette méthode ***
        Constructeur d'un plateau.
        Pour compléter cette méthode vous devez vous référer à la configuration réelle d'un plateau de scrabble.
        Vous pouvez commencer par créer l'attribut cases en considérant qu'aucune case n'est spéciale.
        Regardez ensuite sur un vrai plateau de scrabble quelles positions sont spéciales, créer ces cases spéciales et
         remplacez les anciennes cases.
        """
        super().__init__(parent, height=longueur, width=largeur)
        self.code_couleur = {'VIDE': "#c1bda3", "L2": "#bfd4d6", "M2": "#f6bcaf", "L3": "#3799b2", "M3": "#f86850"}
        # cases blanches
        self.cases = [[Case() for _ in range(Plateau.DIMENSION)] for _ in range(Plateau.DIMENSION)]

        self.delete('case')
        self.delete('lettre')

        for i in range(Plateau.DIMENSION):
            for j in range(Plateau.DIMENSION):
                x1 = i * Plateau.PIXELS_PAR_CASE
                y1 = j * Plateau.PIXELS_PAR_CASE
                x2 = x1 + Plateau.PIXELS_PAR_CASE
                y2 = y1 + Plateau.PIXELS_PAR_CASE
                self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["VIDE"],
                                      outline=Plateau.COULEUR_BORDURE, tags='case')

        for (i, j) in [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)]:
            self.cases[i][j] = Case(3, 'M')

        for (i, j) in [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13),
                       (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]:
            self.cases[i][j] = Case(3, 'L')

        for i in [1, 2, 3, 4]:
            self.cases[i][i] = Case(2, 'M')

            self.cases[i][Plateau.DIMENSION - i - 1] = Case(2, 'M')
            self.cases[Plateau.DIMENSION - i - 1][Plateau.DIMENSION - i - 1] = Case(2, 'M')
            self.cases[Plateau.DIMENSION - i - 1][i] = Case(2, 'M')
        for i, j in [(1, 1), (4, 0), (0, 4), (5, 1), (1, 5), (7, 4), (4, 7)]:
            self.cases[7 - i][7 - j] = Case(2, 'L')
            self.cases[7 + i][7 - j] = Case(2, 'L')
            self.cases[7 - i][7 + j] = Case(2, 'L')
            self.cases[7 + i][7 + j] = Case(2, 'L')
        self.cases[7][7] = Case(2, 'M')
        self.dessiner_plateau()

    def dessiner_plateau(self):
        self.delete('case')
        self.delete('lettre')

        for i in range(Plateau.DIMENSION):
            for j in range(Plateau.DIMENSION):
                x1 = i * Plateau.PIXELS_PAR_CASE
                y1 = j * Plateau.PIXELS_PAR_CASE
                x2 = x1 + Plateau.PIXELS_PAR_CASE
                y2 = y1 + Plateau.PIXELS_PAR_CASE
                self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["VIDE"],
                                      outline=Plateau.COULEUR_BORDURE, tags='case')

        for (i, j) in [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)]:
            # self.cases[i][j] = Case(3, 'M')
            x1 = j * Plateau.PIXELS_PAR_CASE
            y1 = i * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["M3"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1+x2)//2, (y1+y2)//2, font=("purisa", Plateau.FONT_SIZE), justify=CENTER,
                             width=Plateau.PIXELS_PAR_CASE, text="Mot compte triple", tags='case')

        for (i, j) in [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13),
                       (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]:
            # self.cases[i][j] = Case(3, 'L')
            x1 = j * Plateau.PIXELS_PAR_CASE
            y1 = i * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["L3"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1 + x2) // 2, (y1 + y2) // 2, font=("purisa", Plateau.FONT_SIZE),
                             justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                             text="Lettre compte triple", tags='case')

        for i in [1, 2, 3, 4]:
            # self.cases[i][i] = Case(2, 'M')
            x1 = i * Plateau.PIXELS_PAR_CASE
            y1 = i * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["M2"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1 + x2) // 2, (y1 + y2) // 2, font=("purisa", Plateau.FONT_SIZE),
                             justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                             text="Mot compte double")

            # self.cases[i][Plateau.DIMENSION - i - 1] = Case(2, 'M')
            x1 = i * Plateau.PIXELS_PAR_CASE
            y1 = (Plateau.DIMENSION - i - 1) * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["M2"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1 + x2) // 2, (y1 + y2) // 2, font=("purisa", Plateau.FONT_SIZE),
                             justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                             text="Mot compte double")

            # self.cases[Plateau.DIMENSION - i - 1][Plateau.DIMENSION - i - 1]=Case(2, 'M')
            x1 = (Plateau.DIMENSION - i - 1) * Plateau.PIXELS_PAR_CASE
            y1 = (Plateau.DIMENSION - i - 1) * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["M2"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1 + x2) // 2, (y1 + y2) // 2, font=("purisa", Plateau.FONT_SIZE),
                             justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                             text="Mot compte double")

            # self.cases[Plateau.DIMENSION - i - 1][i] = Case(2, 'M')
            x1 = (Plateau.DIMENSION - i - 1) * Plateau.PIXELS_PAR_CASE
            y1 = i * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["M2"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1 + x2) // 2, (y1 + y2) // 2, font=("purisa", Plateau.FONT_SIZE),
                             justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                             text="Mot compte double")

        for i, j in [(1, 1), (4, 0), (0, 4), (5, 1), (1, 5), (7, 4), (4, 7)]:
            # self.cases[7 - i][7 - j] = Case(2, 'L')
            x1 = (7-i) * Plateau.PIXELS_PAR_CASE
            y1 = (7-j) * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["L2"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1 + x2) // 2, (y1 + y2) // 2, font=("purisa", Plateau.FONT_SIZE),
                             justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                             text="Lettre compte double")

            # self.cases[7 + i][7 - j] = Case(2, 'L')
            x1 = (7 + i) * Plateau.PIXELS_PAR_CASE
            y1 = (7 - j) * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["L2"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1 + x2) // 2, (y1 + y2) // 2, font=("purisa", Plateau.FONT_SIZE),
                             justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                             text="Lettre compte double")

            # self.cases[7 - i][7 + j] = Case(2, 'L')
            x1 = (7 - i) * Plateau.PIXELS_PAR_CASE
            y1 = (7 + j) * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["L2"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1 + x2) // 2, (y1 + y2) // 2, font=("purisa", Plateau.FONT_SIZE),
                             justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                             text="Lettre compte double")

            # self.cases[7 + i][7 + j] = Case(2, 'L')
            x1 = (7 + i) * Plateau.PIXELS_PAR_CASE
            y1 = (7 + j) * Plateau.PIXELS_PAR_CASE
            x2 = x1 + Plateau.PIXELS_PAR_CASE
            y2 = y1 + Plateau.PIXELS_PAR_CASE
            self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["L2"],
                                  outline=Plateau.COULEUR_BORDURE, tags='case')
            self.create_text((x1 + x2) // 2, (y1 + y2) // 2, font=("purisa", Plateau.FONT_SIZE),
                             justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                             text="Lettre compte double")

        # self.cases[7][7] = Case(2, 'M')
        x1 = 7 * Plateau.PIXELS_PAR_CASE
        y1 = 7 * Plateau.PIXELS_PAR_CASE
        x2 = x1 + Plateau.PIXELS_PAR_CASE
        y2 = y1 + Plateau.PIXELS_PAR_CASE
        self.create_rectangle(x1, y1, x2, y2, fill=self.code_couleur["M2"], outline=Plateau.COULEUR_BORDURE)
        self.create_text((x1 + x2) // 2, (y1 + y2) // 2, justify=CENTER, width=Plateau.PIXELS_PAR_CASE,
                         text="\u2605", font=("Purisa", Plateau.PIXELS_PAR_CASE-15))

        for i in range(Plateau.DIMENSION):
            for j in range(Plateau.DIMENSION):
                if self.cases[i][j].jeton_occupant is not None:

                    self.dessiner_jeton(self.cases[i][j].jeton_occupant, i, j, Plateau.PIXELS_PAR_CASE)

    @staticmethod
    def code_position_est_valide(code):
        """ *** Vous n'avez pas à coder cette méthode ***
        Méthode statique permettant de valider si un code de positionnement sur le tableau est valide ou pas.
        :param code: str au format « XY » ou « xy » représentant un code de positionnement.
        :return: True si le code passé en argument est un code de positionnement au format « XY » ou « xy » valide.
        En gros, c'est insensible à la casse.
        """
        code = code.upper()
        valide = 2 <= len(code) <= 3 and code[0].isalpha() and code[1:].isdigit()
        if valide:
            index_ligne = ord(code[0]) - ord('A')
            index_colonne = int(code[1:]) - 1
            return 0 <= index_ligne < Plateau.DIMENSION and 0 <= index_colonne < Plateau.DIMENSION
        return False

    @staticmethod
    def decode_position(code):
        """
        Méthode statique servant à transformer un code de positionnement sur le plateau
        en index d'accès de ligne et de colonne sur le plateau.
        :param code: str au format « XY » ou « xy » représentant un code de positionnement.
        :return: tuple (int, int), l'index de la ligne et l'index de la colonne associés au code.
        :exception: Levez une exception avec assert si le code de la position est invalide.
        Pensez à utiliser Plateau.code_position_est_valide.
        """
        assert Plateau.code_position_est_valide(code), "Le code entré est invalide"
        index_ligne = ord(code[0]) - ord("A")
        index_colonne = int(code[1:]) - 1
        return index_ligne, index_colonne

    def case_est_vide(self, position_code):
        """
        Permet de déterminer si une case est vide, c'est-à-dire qu'elle ne contient pas de jeton.
        :param position_code: str, au format « XY » ou « xy » qui un code de positionnement de la case sur le plateau.
         Pensez à réutiliser Plateau.decode_position sur position_code.
        :return: True si la case est vide, False sinon. Rappelez-vous qu'il existe une méthode est_vide disponible pour
         les objets de type Case.
        :exception: Levez une exception avec assert si le code de la position est invalide.
        """
        assert Plateau.code_position_est_valide(position_code), "Le code entré est invalide"

        index_ligne, index_colonne = Plateau.decode_position(position_code)
        return Case.est_vide(self.cases[index_ligne][index_colonne])

    def est_vide(self):
        """
        Permet de déterminer si le plateau est vide, c'est à dire que toutes les cases sont vides.
        :return: True si le plateau est vide, False sinon.
        """
        for i in range(15):
            for j in range(15):
                if not Case.est_vide(self.cases[i][j]):
                    return False

        return True

    def ajouter_jeton(self, jeton,  position_code):
        """
        Permet d'ajouter un jeton dans une case vide du plateau.
        La case est indiquée grâce à son code de positionnement.
        :param jeton: Jeton, le jeton à ajouter sur le plateau.
        :param position_code: str, la position où ajouter (au format « XY » ou « xy »)
        :return: Ne retourne rien.
        :exception: Levez une exception avec assert si le code de la position est invalide ou la case n'est pas vide.
        """
        # assert self.code_position_est_valide(position_code), "Le code entré est invalide"
        # assert self.case_est_vide(position_code), "La case n'est pas vide"

        index_ligne, index_colonne = Plateau.decode_position(position_code)
        self.cases[index_ligne][index_colonne].jeton_occupant = jeton

    def retirer_jeton(self, position_code):
        """
        Permet d'enlever le jeton dans une case du plateau. La case est indiquée grâce à son code de positionnement.
        :param position_code: str, la position où enlever le jeton (au format « XY » ou « xy »).
        :return: Jeton, le jeton à enlever du plateau. Rappelez-vous qu'il existe une méthode retirer_jeton disponible
         pour les objets de type Case.
        :exception: Levez une exception avec assert si le code de la position est invalide ou la case n'est pas vide.
        (inversé car logique originale inverse à ce qu'on veut faire, le assert doit donner erreur si la case est vide,
         donc ok si case n'est pas vide)
        """

        index_ligne, index_colonne = Plateau.decode_position(position_code)

        case = self.cases[index_ligne][index_colonne]
        jeton = Case.retirer_jeton(case)
        return jeton

    def cases_adjacentes_occupees(self, position_code):
        """ *** Vous n'avez pas à coder cette méthode ***
        Étant donnée une position, cette méthode permet de voir si au moins l'une de ses positions voisines est occupée.
        Les cases voisines sont les cases juste en haut, en bas, à gauche et à droite de la case concernée.
        NB: Les cases voisines diagonales ne comptent pas.
        :param position_code: str, la position d'intérêt.
        :return: True si au moins l'une des cases voisines est occupée, False si aucune case voisine n'est occupée.
        :exception: Levez une exception avec assert si le code de la position est invalide
        """
        index_ligne, index_colonne = Plateau.decode_position(position_code)
        voisins = [(index_ligne, index_colonne - 1), (index_ligne, index_colonne + 1), (index_ligne + 1, index_colonne),
                   (index_ligne - 1, index_colonne)]
        voisins = [(i, j) for i, j in voisins if (0 <= i < Plateau.DIMENSION)
                   and (0 <= j < Plateau.DIMENSION)]
        return any([not self.cases[i][j].est_vide() for (i, j) in voisins])

    def valider_positions_avant_ajout(self, positions_codes):
        """ *** Vous n'avez pas à coder cette méthode ***
        Cette méthode implémente certaines règles du jeu donc soyez attentifs au texte ci-dessous.
        Étant données des positions_codes où un utilisateur veut placer ses jetons, cette méthode permet de valider
        s'il peut réelement ajouter les jetons à ces positions.
        Les positions sont valides si:
         - elles sont toutes vides;
         - elles sont toutes sur la même ligne ou la même colonne;
         - une fois qu'elles seront placées sur une même ligne ou une même colonne, elles formeront un mot et pas plus
         sur
         cette même ligne ou colonne. Ici, le mot formé n'est pas important du tout donc n'essayez pas de le trouver;
        Par exemple, si toutes les positions sont sur la ligne 5, votre code doit juste s'assurer qu'entre les positions
        où vous devez ajouter des jetons, des cases ne sont vides.
         - si le plateau est vide, le centre du plateau doit être dans les positions;
         - sinon, au moins une des positions doit être adjacente à une des cases occupées
         du plateau (Pensez à réutilisez cases_adjacentes_occupees et case_est_vide).
        :param positions_codes: str list, liste de string représentant les positions où on veut ajouter des jetons.
        :return: True si les positions sont valides, False sinon.
        :exception: Levez une exception avec assert si le code d'une des positions est invalide.
        """
        positions_decodees = [Plateau.decode_position(p) for p in positions_codes]

        lignes, cols = zip(*positions_decodees)
        lignes, cols = list(set(lignes)), list(set(cols))
        meme_ligne, meme_col = len(lignes) == 1, len(cols) == 1
        valide = meme_ligne or meme_col

        valide = valide

        if valide:
            if self.cases[7][7].jeton_occupant is None:
                valide = (7, 7) in positions_decodees
            else:
                valide = any([self.cases_adjacentes_occupees(pos) for pos in positions_codes])
            if valide and meme_ligne:
                ligne, n, m = lignes[0], min(cols), max(cols)
                valide = all([(not self.cases[ligne][i].est_vide()) for i in range(n, m + 1) if i not in cols])
            elif valide and meme_col:
                col, n, m = cols[0], min(lignes), max(lignes)
                valide = all([(not self.cases[i][col].est_vide()) for i in range(n, m + 1) if i not in lignes])
        return valide

    def placer_mots(self, jetons_a_ajouter, position_codes):
        """
        Permet de placer plusieurs jetons sur le plateau afin de former un ou plusieurs mots.
        Pensez à réutiliser valider_positions_avant_ajout.
        :param jetons_a_ajouter: Jetons à ajouter pour placer nos mots.
        :param position_codes: str list, liste de chaînes de caractères représentant les positions où on veut placer
         les jetons.
        :return: tuple de type (str list, int):
            - Le premier élement est la liste des mots formés avec les jetons si l'ajout a été fait, liste vide sinon.
            - Le second élément est le score obtenu si l'ajout a été fait, 0 sinon.
        :exception: Levez une exception avec assert si les positions sont invalides.
        """

        for i in range(len(jetons_a_ajouter)):
            self.ajouter_jeton(jetons_a_ajouter[i], position_codes[i])

        return self.mots_score_obtenus(position_codes)[0], self.mots_score_obtenus(position_codes)[1]

    def mots_score_obtenus(self, nouvelles_positions):
        """ *** Vous n'avez pas à coder cette méthode ***
        Trouver les mots ajoutés et le score total obtenu lorsque le joueur vient juste d'ajouter des jetons aux
        positions de la liste en argument.
        :param nouvelles_positions: str list, liste de chaînes de caractères représentant les dernières positions où
        des jetons ont été ajoutés.
        :return: L'ensemble des mots formés par l'ajout de jetons aux nouvelles positions.
        """
        positions_decodees = [Plateau.decode_position(p) for p in nouvelles_positions]
        score_total = 0
        lignes, cols = zip(*positions_decodees)
        mots = []

        for ligne in set(lignes):
            # positions_decodees remplacé par nouvelles_positions
            lmots, score = self.__mots_et_score_sur_ligne_ou_colonne(nouvelles_positions, ligne)
            mots += lmots
            score_total += score
        for col in set(cols):
            # positions_decodees remplacé par nouvelles_positions
            lmots, score = self.__mots_et_score_sur_ligne_ou_colonne(nouvelles_positions, colonne=col)
            mots += lmots
            score_total += score
        return mots, score_total

    def __mots_et_score_sur_ligne_ou_colonne(self, nouvelles_positions, ligne=None, colonne=None):
        """ *** Vous n'avez pas à coder cette méthode ***
        Permet de trouver les mots sur une ligne ou une colonne et le score associé.
        :param nouvelles_positions:  str list, liste de chaînes de caractères représentant les dernières
        positions où des jetons ont été ajoutés.
        :param ligne: (int, optionel), index de la ligne d'intérêt
        :param colonne: (int, optionel), index de la colonne d'intérêt
        :return: tuple (str list, int), la liste des mots trouvés sur la ligne ou la colonne et le score total.
        Plus précisément la liste devra contenir au maximum un élément car un tout nouvel ajout de jetons ne peut pas
        créer plus d'un mot sur la même ligne ou colonne.
        :exception: Levez une exception avec assert si la ligne et la colonne sont spécifiées ou aucun des deux ne
         l'est.
        """
        assert (ligne is None) ^ (colonne is None), "Précisez seulement la ligne ou la colonne, pas les deux."
        positions_decodees = [Plateau.decode_position(p) for p in nouvelles_positions]
        mots, score_total = [], 0
        mot, score_mot, multiplicateur, pos_mot = "", 0, 1, []

        for i in range(Plateau.DIMENSION):
            pos = (ligne, i) if ligne is not None else (i, colonne)
            case = self.cases[pos[0]][pos[1]]
            if case.est_vide():
                if len(mot) > 1 and any([p in pos_mot for p in positions_decodees]):
                    mots.append(mot)
                    score_total += score_mot * multiplicateur
                mot, score_mot, multiplicateur, pos_mot = "", 0, 1, []
            else:
                mot += case.lettre_jeton()
                pos_mot.append(pos)
                if pos in positions_decodees and case.type == "L":
                    score_mot += case.valeur_jeton() * case.multiplicateur
                else:
                    score_mot += case.valeur_jeton()
                if pos in positions_decodees and case.type == "M":
                    multiplicateur *= case.multiplicateur
        if len(mot) > 1 and any([p in pos_mot for p in positions_decodees]):
            mots.append(mot)
            score_total += score_mot * multiplicateur
        return mots, score_total

    def redimensionner(self, event):
        new_dim = min(event.width, event.height)
        self.nb_pixels_per_case = new_dim // Plateau.DIMENSION
        self.dessiner()

    def dessiner(self):

        for i in range(self.DIMENSION):
            for j in range(Plateau.DIMENSION, ):

                debut_ligne, debut_colonne, fin_ligne, fin_colonne = Plateau.coord_case(i, j, Plateau.PIXELS_PAR_CASE)

            # On dessine le rectangle. On utilise l'attribut "tags" pour être en mesure de récupérer les éléments
            # par la suite.
                self.create_rectangle(debut_colonne, debut_ligne, fin_colonne,fin_ligne,
                                      fill=self.cases[i][j].code_couleur, tags='case')

                delta = int(Plateau.PIXELS_PAR_CASE/2.)
                if i == j and i == 7:
                    self.create_text((Plateau.debut_colonne + delta, Plateau.debut_ligne + delta), justify=CENTER,
                                 font=('Times', '{}'.format(delta)), text='\u2605', tags='case')
                else:
                    self.create_text((Plateau.debut_colonne + delta, Plateau.debut_ligne + delta),
                                 font=('Times', '{}'.format(int(delta/2))),
                                 justify=CENTER, text=self.cases[i][j].text_case, tags='case')
                if not self.cases[i][j].est_vide():
                    Plateau.dessiner_jeton(self.cases[i][j].jeton_occupant, i, j, self.nb_pixels_per_case)

    # code du prof
    def coord_case(i, j, nb_pixels_per_case):
        debut_ligne = i * nb_pixels_per_case
        fin_ligne = debut_ligne + nb_pixels_per_case
        debut_colonne = j * nb_pixels_per_case
        fin_colonne = debut_colonne + nb_pixels_per_case
        return debut_ligne, debut_colonne, fin_ligne, fin_colonne

    # code du prof
    def dessiner_jeton(self, jeton, i, j, nb_pixels_per_case, tag='lettre'):
        d = nb_pixels_per_case//2
        debut_ligne, debut_colonne, fin_ligne, fin_colonne = Plateau.coord_case(i, j, nb_pixels_per_case)


        self.create_rectangle(debut_colonne, debut_ligne, fin_colonne, fin_ligne, fill='#b9936c', tags='lettre')
        self.create_text((debut_colonne + d, debut_ligne + d),
                         font=('Times', '{}'.format(int(nb_pixels_per_case*.5))), text=str(jeton), tags='lettre')
