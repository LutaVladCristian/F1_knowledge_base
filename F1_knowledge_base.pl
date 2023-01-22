%Student: Luta VLad Cristian
%Grupa: 341A2

% Student exercise profile
:- set_prolog_flag(occurs_check, error).        % disallow cyclic terms
:- set_prolog_stack(global, limit(8 000 000)).  % limit term space (8Mb)
:- set_prolog_stack(local,  limit(2 000 000)).  % limit environment space


%Fapte
%piloti
pilot(hamilton).
pilot(bottas).
pilot(verstappen).
pilot(leclerc).
pilot(latifi).
pilot(sainz).
pilot(schumacher).
pilot(perez).
pilot(tsunoda).
pilot(stroll).
pilot(alonso).
pilot(vettel).
pilot(russel).
pilot(magnussen).
pilot(ocon).
pilot(zhou).
pilot(ricciardo).
pilot(norris).
pilot(albon).
pilot(gasly).

% curse neterminate
cursa_neterminata(latifi, bahrain).
cursa_neterminata(leclerc,saudi_arabia).
cursa_neterminata(verstappen,australia).
cursa_neterminata(verstappen,emilia_romagna).
cursa_neterminata(leclerc,miami).
cursa_neterminata(verstappen,spania).
cursa_neterminata(sainz,monaco).
cursa_neterminata(verstappen,azerbaijan).
cursa_neterminata(sainz,canada).
cursa_neterminata(zhou,uk).
cursa_neterminata(verstappen,austria).
cursa_neterminata(leclerc,franta).
cursa_neterminata(magnussen,ungaria).
cursa_neterminata(schumacher,olanda).
cursa_neterminata(schumacher,italia).
cursa_neterminata(latifi,belgia).
cursa_neterminata(gasly,singapore).
cursa_neterminata(verstappen,us).
cursa_neterminata(latifi,japonia).
cursa_neterminata(latifi,mexic).
cursa_neterminata(schumacher,brazilia).
cursa_neterminata(hamilton,abu_dhabi).

% tipul de pneuri
pneuri(soft).
pneuri(mediu).
pneuri(hard).
pneuri(wet).
pneuri(intermediar).

% tipul de uzura pneuri
uzura(consumate).
uzura(noi).
uzura(performance).

% castigatorii fiecarei curse
pilot_cursa(leclerc, bahrain, 1).
pilot_cursa(verstappen, saudi_arabia, 1).
pilot_cursa(leclerc, australia, 1).
pilot_cursa(verstappen, emilia_romagna, 1).
pilot_cursa(verstappen, miami, 1).
pilot_cursa(verstappen, spain, 1).
pilot_cursa(perez, monaco, 1).
pilot_cursa(verstappen, azerbaijan, 1).
pilot_cursa(verstappen, canada, 1).
pilot_cursa(sainz, uk, 1).
pilot_cursa(verstappen, franta, 1).
pilot_cursa(verstappen, ungaria, 1).
pilot_cursa(verstappen, belgia, 1).
pilot_cursa(verstappen, olanda, 1).
pilot_cursa(verstappen, italia, 1).
pilot_cursa(perez, singapore, 1).
pilot_cursa(verstappen, japonia, 1).
pilot_cursa(verstappen, us, 1).
pilot_cursa(verstappen, mexic, 1).
pilot_cursa(russel, brazilia, 1).
pilot_cursa(verstappen, abu_dhabi, 1).

% apartenenta la echipa
pilot_echipa(hamilton, mercedes).
pilot_echipa(russel, mercedes).
pilot_echipa(verstappen, red_bull).
pilot_echipa(perez, red_bull).
pilot_echipa(leclerc, ferrari).
pilot_echipa(sainz, ferrari).
pilot_echipa(gasly, alphatauri).
pilot_echipa(tsunoda, alphatauri).
pilot_echipa(bottas, alfa_romeo).
pilot_echipa(zhou, alfa_romeo).
pilot_echipa(ricciardo, mclaren).
pilot_echipa(norris, mclaren).
pilot_echipa(latifi, williams).
pilot_echipa(albon, williams).
pilot_echipa(magnussen, haas).
pilot_echipa(schumacher, haas).
pilot_echipa(alonso, alpine).
pilot_echipa(ocon, alpine).
pilot_echipa(stroll, aston_martin).
pilot_echipa(vettel, aston_martin).


%Prelucrari Liste
%determinarea apartenenta la o lista
is_member(X, [X | _]) :- !.

is_member(X, [_ | Rest]) :-
    is_member(X, Rest).

%numarare elemente din lista
list_length([], 0).

list_length([_ | L], N) :-
    list_length(L, N1),
    N is N1 + 1.

%eliminare duplicate in lista
eliminate_duplicates(L, R) :-
    eliminate_duplicates(L, [], R).

eliminate_duplicates([], _, []).

eliminate_duplicates([H|T], L, R) :-
    member(H, L),
    eliminate_duplicates(T, L, R).
eliminate_duplicates([H|T], L, [H|R]) :-
    \+ member(H, L),
    eliminate_duplicates(T, [H|L], R).


%Reguli
masina(Pilot, Pneuri, Echipa):-
    pilot_echipa(Pilot, Echipa),
    pneuri(Pneuri).

castigator_cursa(Pilot):- 
    pilot_cursa(Pilot, _, 1), !.

pilot_echipa_castigatoare(Pilot, Echipa):-
    pilot_cursa(Pilot, _, 1), !,
	pilot_echipa(Pilot, Echipa).

curse_castigate(Pilot, Ans):-
	findall(Cursa, pilot_cursa(Pilot, Cursa, 1), Ans).

echipa_curse_castigate(Echipa, Ans):-
	findall(Cursa, (pilot_cursa(Pilot, Cursa, 1), pilot_echipa(Pilot, Echipa)), Ans).

cate_curse_castigate(Pilot, N):-
    findall(Cursa, pilot_cursa(Pilot, Cursa, 1), Ans),
	list_length(Ans, N).

cate_curse_castigate_echipa(Echipa, N):-
    findall(Cursa, (pilot_cursa(Pilot, Cursa, 1), pilot_echipa(Pilot, Echipa)), Ans),
	list_length(Ans, N).

ce_piloti_castigatori_cursa(Ans):-
    findall(Pilot, pilot_cursa(Pilot, _, 1), Lista),
    eliminate_duplicates(Lista, Ans), !.

ce_echipe_castigatoare_cursa(Ans):-
    findall(Echipa, (pilot_cursa(Pilot, _, 1), pilot_echipa(Pilot, Echipa)), Lista),
    eliminate_duplicates(Lista, Ans), !.
    
piloti_dnf(Ans):-
    findall(Pilot, cursa_neterminata(Pilot, _), Lista),
	eliminate_duplicates(Lista, Ans), !.
    
echipe_dnf(Ans):-  
	findall(Echipa, (cursa_neterminata(Pilot, _), pilot_echipa(Pilot, Echipa)), Lista),
	eliminate_duplicates(Lista, Ans), !.

pit_stop(Pilot, Echipa, Pneuri, Uzura):-
    masina(Pilot, Pneuri, Echipa),
    Uzura == consumate.

strategie(Vreme, Pneuri):-
    Vreme == calda,
    is_member(Pneuri, [mediu, soft]), !.

strategie(Vreme, Pneuri):-
    Vreme == umeda,
    is_member(Pneuri, [mediu, hard, intermediar]), !.

strategie(Vreme, Pneuri):-
    Vreme == ploioasa,
    is_member(Pneuri, [intermediar, wet]), !.

depasire(Pilot1, Pneuri1, Uzura1, Pilot2, Pneuri2, Uzura2, Vreme):-
    strategie(Vreme, Pneuri1),
    not(strategie(Vreme, Pneuri2)),
    pilot(Pilot1),
    uzura(Uzura1),
    uzura(Uzura2),
    pilot(Pilot2).

depasire(Pilot1, Pneuri1, Uzura1, Pilot2, Pneuri2, Uzura2, Vreme):-    
    strategie(Vreme, Pneuri1),
    strategie(Vreme, Pneuri2),
    pilot(Pilot1),
    pilot(Pilot2),
    is_member(Uzura1, [noi]), !,
    not(is_member(Uzura2, [performance])), !.

depasire(Pilot1, Pneuri1, Uzura1, Pilot2, Pneuri2, Uzura2, Vreme):-    
    strategie(Vreme, Pneuri1),
    strategie(Vreme, Pneuri2),
    pilot(Pilot1),
    pilot(Pilot2),    
    is_member(Uzura1, [performance]), !,
	is_member(Uzura2, [noi, consumate]), !.

depasire(Pilot1, Pneuri1, Uzura1, Pilot2, Pneuri2, Uzura2, Vreme):-    
    strategie(Vreme, Pneuri1),
    strategie(Vreme, Pneuri2),
    pilot(Pilot1),
    pilot(Pilot2),
    not(is_member(Uzura1, [consumate])), !,
    uzura(Uzura2).

