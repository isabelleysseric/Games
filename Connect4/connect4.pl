
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%    LES ETATS   %%%%%%%%%%%%%%%%%%%


%  Board:         1    2    3    4    5
%            a   a1   a2   a3   a4   a5
%            b   b1   b2   b3   b4   b5
%            c   c1   c2   c3   c4   c5
%            d   d1   d2   d3   d4   d5
%            e   e1   e2   e3   e4   e5
%            f   f1   f2   f3   f4   f5
%
%  Liste qui représente le board:
%      p4(a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,
%         d1,d2,d3,d4,d5,e1,e2,e3,e4,e5,f1,f2,f3,f4,f5,
%         JOUEUR_ACTIF)
%
%  _ :  La valeur de la case peut être n'importe quoi
%  J :  La case doit être occupée par une pièce du joueur
%


%Etat initial
etat_initial(p4(v,v,v,v,v
               ,v,v,v,v,v
               ,v,v,v,v,v
               ,v,v,v,v,v
               ,v,v,v,v,v,x)).

% Combinaisons gagnantes - Horizontales ligneA
etat_final(p4(J,J,J,J,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,J,J,J,J
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_,_),J) :- not(J=v).


% Combinaisons gagnantes - Horizontales ligneB
etat_final(p4(_,_,_,_,_
             ,J,J,J,J,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,_
             ,_,J,J,J,J
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_,_),J) :- not(J=v).


% Combinaisons gagnantes - Horizontales ligneC
etat_final(p4(_,_,_,_,_
             ,_,_,_,_,_
             ,J,J,J,J,_
             ,_,_,_,_,_
             ,_,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,_
             ,_,_,_,_,_
             ,_,J,J,J,J
             ,_,_,_,_,_
             ,_,_,_,_,_,_),J) :- not(J=v).


% Combinaisons gagnantes - Horizontales ligneD
etat_final(p4(_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,J,J,J,J,_
             ,_,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,J,J,J,J
             ,_,_,_,_,_,_),J) :- not(J=v).


% Combinaisons gagnantes - Horizontales ligneE
etat_final(p4(_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,J,J,J,J,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,_,_,_,_
             ,_,J,J,J,J,_),J) :- not(J=v).


% Combinaisons gagnantes - Colonnes Verticales
etat_final(p4(J,_,_,_,_
             ,J,_,_,_,_
             ,J,_,_,_,_
             ,J,_,_,_,_
             ,_,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,_
             ,J,_,_,_,_
             ,J,_,_,_,_
             ,J,_,_,_,_
             ,J,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,J,_,_,_
             ,_,J,_,_,_
             ,_,J,_,_,_
             ,_,J,_,_,_
             ,_,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,_
             ,_,J,_,_,_
             ,_,J,_,_,_
             ,_,J,_,_,_
             ,_,J,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,J,_,_
             ,_,_,J,_,_
             ,_,_,J,_,_
             ,_,_,J,_,_
             ,_,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,_
             ,_,_,J,_,_
             ,_,_,J,_,_
             ,_,_,J,_,_
             ,_,_,J,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,J,_
             ,_,_,_,J,_
             ,_,_,_,J,_
             ,_,_,_,J,_
             ,_,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,_
             ,_,_,_,J,_
             ,_,_,_,J,_
             ,_,_,_,J,_
             ,_,_,_,J,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,J
             ,_,_,_,_,J
             ,_,_,_,_,J
             ,_,_,_,_,J
             ,_,_,_,_,_,_),J) :- not(J=v).

etat_final(p4(_,_,_,_,_
             ,_,_,_,_,J
             ,_,_,_,_,J
             ,_,_,_,_,J
             ,_,_,_,_,J,_),J) :- not(J=v).



% Combinaisons gagnantes - Diagonales Descendantes
 etat_final(p4(J,_,_,_,_
              ,_,J,_,_,_
              ,_,_,J,_,_
              ,_,_,_,J,_
              ,_,_,_,_,_,_),J) :- not(J=v).

 etat_final(p4(_,J,_,_,_
              ,_,_,J,_,_
              ,_,_,_,J,_
              ,_,_,_,_,J
              ,_,_,_,_,_,_),J) :- not(J=v).

 etat_final(p4(_,_,_,_,_
              ,J,_,_,_,_
              ,_,J,_,_,_
              ,_,_,J,_,_
              ,_,_,_,J,_,_),J) :- not(J=v).

 etat_final(p4(_,_,_,_,_
              ,_,J,_,_,_
              ,_,_,J,_,_
              ,_,_,_,J,_
              ,_,_,_,_,J,_),J) :- not(J=v).


 etat_final(p4(_,_,_,J,_
              ,_,_,J,_,_
              ,_,J,_,_,_
              ,J,_,_,_,_
              ,_,_,_,_,_,_),J) :- not(J=v).

 etat_final(p4(_,_,_,_,J
              ,_,_,_,J,_
              ,_,_,J,_,_
              ,_,J,_,_,_
              ,_,_,_,_,_,_),J) :- not(J=v).

 etat_final(p4(_,_,_,_,_
              ,_,_,_,J,_
              ,_,_,J,_,_
              ,_,J,_,_,_
              ,J,_,_,_,_,_),J) :- not(J=v).

 etat_final(p4(_,_,_,_,_
              ,_,_,_,_,J
              ,_,_,_,J,_
              ,_,_,J,_,_
              ,_,J,_,_,_,_),J) :- not(J=v).



% Combinaison de la partie nulle
% *voir la section suivante pour la définition des variables
etat_final(p4(  A1,A2,A3,A4,A5,
                B1,B2,B3,B4,B5,
                C1,C2,C3,C4,C5,
                D1,D2,D3,D4,D5,
                E1,E2,E3,E4,E5,_),J) :-
                    not(A1=v), not(A2=v), not(A3=v), not(A4=v), not(A5=v),
                    not(B1=v), not(B2=v), not(B3=v), not(B4=v), not(B5=v),
                    not(C1=v), not(C2=v), not(C3=v), not(C4=v), not(C5=v),
                    not(D1=v), not(D2=v), not(D3=v), not(D4=v), not(D5=v),
                    not(E1=v), not(E2=v), not(E3=v), not(E4=v), not(E5=v).


% Changement de joueur
n(x,o).
n(o,x).



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%    LES OPERATIONS   %%%%%%%%%%%%%%%%

% Changement d'un ETAT à un ETAT suivant
%  PARAM     1er -Nom de la case (pour faire un choix)
%            2e  -ETAT de départ (avant de jouer)
%            3e  -Commande a faire entre ETAT et ETAT_SUIVANT
%            4e  -ETAT du board après avoir joué la case (1er param)
%
%  Lorsque les nom sont en majuscules dans les ETATS, sont sont des
%  variables qui peuvent prendre 3 valeurs:     x: Joueur1
%                                               o: Joueur2
%                                               v: vide


% Opérations sur ligneA
operation(a1,
          p4(v,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,A1),
          p4(J1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(a2,
          p4(A1,v,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,A2),
          p4(A1,J1,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(a3,
          p4(A1,A2,v,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,A3),
          p4(A1,A2,J1,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(a4,
          p4(A1,A2,A3,v,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,A4),
          p4(A1,A2,A3,J1,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(a5,
          p4(A1,A2,A3,A4,v,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,A5),
          p4(A1,A2,A3,A4,J1,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).

% Opérations sur la ligneB
operation(b1,
          p4(A1,A2,A3,A4,A5,
             v,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,B1),
          p4(A1,A2,A3,A4,A5,
             J1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(b2,
          p4(A1,A2,A3,A4,A5,
             B1,v,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,B2),
          p4(A1,A2,A3,A4,A5,
             B1,J1,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(b3,
          p4(A1,A2,A3,A4,A5,
             B1,B2,v,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,B3),
          p4(A1,A2,A3,A4,A5,
             B1,B2,J1,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(b4,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,v,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,B4),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,J1,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(b5,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,v,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,B5),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,J1,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).

% Opérations sur la ligneC
operation(c1,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             v,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,C1),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             J1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(c2,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,v,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,C2),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,J1,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(c3,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,v,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,C3),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,J1,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(c4,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,v,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,C4),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,J1,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(c5,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,v,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,C5),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,J1,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).

% Opérations sur la ligneD
operation(d1,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             v,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,D1),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             J1,D2,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(d2,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,v,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,D2),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,J1,D3,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(d3,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,v,D4,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,D3),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,J1,D4,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(d4,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,v,D5,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,D4),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,J1,D5,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(d5,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,v,
             E1,E2,E3,E4,E5,
             J1),
          tracer(J1,D5),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,J1,
             E1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).

% Opérations sur la ligneE
operation(e1,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             v,E2,E3,E4,E5,
             J1),
          tracer(J1,E1),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             J1,E2,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(e2,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,v,E3,E4,E5,
             J1),
          tracer(J1,E2),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,J1,E3,E4,E5,
             J2))
          :- n(J1,J2).
operation(e3,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,v,E4,E5,
             J1),
          tracer(J1,E3),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,J1,E4,E5,
             J2))
          :- n(J1,J2).
operation(e4,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,v,E5,
             J1),
          tracer(J1,E4),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,J1,E5,
             J2))
          :- n(J1,J2).
operation(e5,
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,v,
             J1),
          tracer(J1,E5),
          p4(A1,A2,A3,A4,A5,
             B1,B2,B3,B4,B5,
             C1,C2,C3,C4,C5,
             D1,D2,D3,D4,D5,
             E1,E2,E3,E4,J1,
             J2))
          :- n(J1,J2).




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%% AFFICHAGE %%%%%%%%%%%%%%%%%%%%%%%%

% Affichage de la grille
afficher_grille(p4(A1,A2,A3,A4,A5,
                   B1,B2,B3,B4,B5,
                   C1,C2,C3,C4,C5,
                   D1,D2,D3,D4,D5,
                   E1,E2,E3,E4,E5,_)) :-
    write("   "), write(" 1  "), write(" 2  "), write(" 3  "), write(" 4  "), write(" 5  "), nl,
    write("a "), trou(A1),trou(A2),trou(A3),trou(A4),trou(A5),writeln('|'),
    write("b "), trou(B1),trou(B2),trou(B3),trou(B4),trou(B5),writeln('|'),
    write("c "), trou(C1),trou(C2),trou(C3),trou(C4),trou(C5),writeln('|'),
    write("d "), trou(D1),trou(D2),trou(D3),trou(D4),trou(D5),writeln('|'),
    write("e "), trou(E1),trou(E2),trou(E3),trou(E4),trou(E5),writeln('|'),
    nl.

%Affiche la case
trou(Jeton) :-
    write('| '),
    switch(Jeton, [v: write(' '), x: write('○'), o: write('●')]),
    write(' ').

%Affiche le choix du joueur (MOVE effectué)
afficher_operation(CASE, tracer(Joueur, Case)) :-
    write('Joueur '),
    switch(Joueur, [v: write(' '), x: write('○'), o: write('●')]),
    write(' joue à '),
    writeln(CASE).

%Affiche le joueur gagnant
afficher_gagnant(Joueur) :-
    switch(Joueur, [v: write("La partie est nulle, personne ne"),
                    x: write('○'),
                    o: write('●')]),
    write(" gagne la partie!"), nl.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%   FONCTIONS UTILITAIRES    %%%%%%%%%%%%%%


% switch/2 simule le switch procédural
% PARAM     X:     Variable qui correspond a la fonction a faire
%           Val:   La valeur de la variable
%           Goal:  La fonction a effectuer
%
switch(X, [Val:Goal|Cases]) :-
    ( X=Val -> call(Goal) ; switch(X, Cases) ).


%Sert à remplacer une valeur par une autre
% PARAM     X:   Variable a changer
%           Val: Valeur de la variable
%           New: Valeur qui remplacera Val
%
remplacement(X, [Val:New|Cases], Y) :-
    ( X=Val -> Y=New ; remplacement(X, Cases, Y) ).


%Met à jour la liste de cases disponibles
% PARAM    CASE:  La case qui sera jouée
%          Liste: La liste de choix de case avant la modification
%          NouvelleListe: La liste de choix après que le coup soit joué
%
update_list( Case, Liste, NouvelleListe):-
    %On cherche la nouvelle case que l'on peut atteindre
    remplacement(Case, [e1: d1, d1: c1, c1: b1, b1: a1, a1: rien,
                        e2: d2, d2: c2, c2: b2, b2: a2, a2: rien,
                        e3: d3, d3: c3, c3: b3, b3: a3, a3: rien,
                        e4: d4, d4: c4, c4: b4, b4: a4, a4: rien,
                        e5: d5, d5: c5, c5: b5, b5: a5, a5: rien],
                 NouvelleCase),

    %On ajoute la nouvelle case à la nouvelle liste, si on est rendu au top, on rajoute rien
    (   not(NouvelleCase=rien)
        -> append([NouvelleCase],Liste, LISTE1)
         ; append([], Liste, LISTE1) ),
    %On enlève la case qui vient d'être jouée
    delete(LISTE1, Case, NouvelleListe).




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% PARTIE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

connect4 :-
   %Les cases permises au départ
   LIST =[e1,e2,e3,e4,e5],
   etat_initial(E), jeu(LIST,E,GAGNANT).


jeu(LIST,ETAT, GAGNANT) :-
    etat_final(ETAT, GAGNANT),!,
    afficher_grille(ETAT),
    afficher_gagnant(GAGNANT).

jeu(LIST, ETAT, GAGNANT) :-
    afficher_grille(ETAT),
    choisir_operation(LIST, ETAT, NEWLIST, ETAT_SUIVANT),
    jeu( NEWLIST, ETAT_SUIVANT, GAGNANT ).





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% ALGORITHME %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

choisir_operation( Liste, ETAT, NouvelleListe, ETAT_SUIVANT):-
    choisirMAX(ETAT, Liste, Liste, CASE, ETAT_SUIVANT, NouvelleListe),
    sleep(0.5).

%Test si cet si
testerVictoireMAX(ETAT, []):-false.
testerVictoireMAX(ETAT, [X|LISTE]):-
    operation(X,ETAT,OP,ETAT_SUIVANT),
    (   etat_final(ETAT_SUIVANT,GAGNANT) -> true ; testerVictoireMAX(ETAT, LISTE)).

testerVictoireMIN(ETAT, []):-false.
testerVictoireMIN(ETAT, [X|LISTE]):-
    update_list(X, [X|LISTE], NouvelleListe),
    operation(X,ETAT,OP,ETAT_SUIVANT),
    (   testerVictoireMAX(ETAT_SUIVANT, NouvelleListe) -> true; testerVictoireMIN(ETAT, LISTE)).

% Fin de la recherche, affichage, operation, etc.
choisirMAX(ETAT,LISTE_ORIG,[], CHOIX,ETAT_FINAL, NEWLIST):-
                      operation( CHOIX, ETAT, OP, ETAT_FINAL ),
                      afficher_operation(CHOIX, OP),
                      update_list( CHOIX, LISTE_ORIG, NEWLIST).

%Recherche d'un coup gagnant
choisirMAX(ETAT, LISTE_ORIG,Liste, CHOIX,ETAT_FINAL,NEWLIST):-
                    %on choisi aléatoirement un élément de la liste pour rendre ça plus intéressant
                    random_member(X,Liste),
                    delete(Liste,X,LISTE),
                    update_list(X,Liste,NouvelleListe),
                    operation(X,ETAT,OP,ETAT_SUIVANT),
     % on analyse l'état obtenu après ce mouvement
    (    testerVictoireMAX(ETAT, NouvelleListe)
               %Si oui, on a trouvé notre choix
               -> choisirMAX(ETAT, LISTE_ORIG, [], X, ETAT_FINAL, NEWLIST)
               %Sinon, on vérifie que ce mouvement ne fera pas gagner MIN le tour après
               ;  %Teste si ce move peut permettre a MIN de gagne rendu a son tour
                  (   testerVictoireMIN(ETAT_SUIVANT, NouvelleListe)
                      %Si la case permet a MIN de gagner, on recommence la recherche en l'enlevant des choix
                      ->  (   length(NouvelleListe,1)
                                     %Si on a qu'un choix, on le prend....
                                     -> choisirMAX(ETAT, LISTE_ORIG, [], X, ETAT_FINAL, NEWLIST)
                                     %Sinon en cherche avec une autre possibilité
                                     ;   choisirMAX(ETAT, LISTE_ORIG, LISTE, CHOIX, ETAT_FINAL, NEWLIST))
                      ;%Sinon on prend ce choix car il ne permet pas à MIN de gagner au moins
                       choisirMAX(ETAT, LISTE_ORIG, [], X, ETAT_FINAL, NEWLIST)
                  )
     ).

















