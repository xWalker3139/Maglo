from django.conf.urls import url
from my_app import views

app_name = "my_app"

urlpatterns = [

    ###################COPIL###########################
    url(r'^inregistrare_copil', views.inregistrare_copil, name="inregistrare_copil"),
    url(r'^posteaza_anunt_copil/$', views.posteaza_anunt_copil, name="posteaza_anunt_copil"),
    url(r'^contul_meu_copil/$', views.contul_meu_copil, name="contul_meu_copil"),
    url(r'^deconectare_copil/$', views.deconectare_copil1, name="deconectare_copil1"),
    url(r'^autentificate_copil/$', views.autentificate_copil, name="autentificate_copil"),
    url(r'^anunturi_totale_copil/$', views.anunturi_totale_copil, name="anunturi_totale_copil"),
    url(r'^pag_anunturi_copil/(?P<pk>\d+)/$', views.pag_anunturi_copil, name="pag_anunturi_copil"),
    url(r'^anunturi_favorite_c/$', views.anunturi_favorite_copil, name="anunturi_favorite_copil"),
    url(r'^update_copil/(?P<pk>\d+)/$', views.update_copil, name="update_copil"),
    url(r'^pag_update_copil/$', views.pag_update_copil, name='pag_update_copil'),
    url(r'^delete_copil/(?P<pk>\d+)/$', views.delete_copil, name="delete_copil"),
    url(r'^pag_delete_copil/$', views.pag_delete_copil, name="pag_delete_copil"),
    url(r'^actualizare_date_copil/(?P<pk>\d+)/$', views.actualizare_date_copil, name="actualizare_date_copil"),
    url(r'^schimbare_parola/(?P<pk>\d+)/$', views.schimb_parola_copil, name="schimb_parola_copil"),
    ###################CATEGORII_COPIL#################
    url(r'^pag_anunturi_postate/(?P<pk>\d+)/$', views.pag_anunturi_postate, name="pag_anunturi_postate"),
    url(r'^carti_copil/$', views.carti_copil, name="carti_copil"),
    url(r'^pag_carti_copil/(?P<pk>\d+)/$', views.pag_carti_copil, name="pag_carti_copil"),
    url(r'^jucarii/$', views.jucarii_copil, name="jucarii_copil"),
    url(r'^pag_jucarii_copil/(?P<pk>\d+)/$', views.pag_jucarii_copil, name="pag_jucarii_copil"),
    url(r'^haine_copil/$', views.haine_copil, name="haine_copil"),
    url(r'^pag_haine_copil/(?P<pk>\d+)/$', views.pag_haine_copil, name="pag_haine_copil"),
    url(r'^articole_sportive_copil/$', views.articole_sportive_copil, name="articole_sportive_copil"),
    url(r'^pag_articole_sportive_copil/(?P<pk>\d+)/$', views.pag_articole_sportive, name="pag_articole_sportive"),
    url(r'^schimburi_copil/$', views.schimburi_copil, name="schimburi_copil"),
    url(r'^pag_schimburi_copil/(?P<pk>\d+)/$', views.pag_schimburi_copil, name="pag_schimburi_copil"),
    url(r'^mama_si_copil/$', views.mama_si_copil, name="mama_si_copil"),
    url(r'^pag_mama_si_copil/(?P<pk>\d+)/$', views.pag_mama_si_copil, name="pag_mama_si_copil"),
    
    #####################ADULT#########################

    url(r'^inregistrare_adult/$', views.inregistrare_adult, name="inregistrare_adult"),
    url(r'contul_meu_adult/$', views.contul_meu_adult, name="contul_meu_adult"),
    url(r'^posteaza_anunt_adult/$', views.posteaza_anunt_adult, name="posteaza_anunt_adult"),
    url(r'^deconectare_adult/$', views.deconectare_adult, name="deconectare_adult"),
    url(r'^deconectare_adult1/$', views.deconectare_adult1, name="deconectare_adult1"),
    url(r'^autentificate_adult/$', views.autentificate_adult, name="autentificate_adult"),
    url(r'^anunturi_favorite_d/$', views.anunturi_favorite_d, name="anunturi_favorite_d"),
    url(r'update_adult/(?P<pk>\d+)/$', views.UpdateAdult, name="update_adult"),
    url(r'^pag_update_adult/$', views.pag_update_adult, name="pag_update_adult"),
    url(r'^delete_adult/(?P<pk>\d+)/$', views.DeleteAdult, name="delete_adult"),
    url(r'^pag_delete_adult/$', views.pag_delete_adult, name="pag_delete_adult"),
    url(r'^actualizeaza_date_adult/(?P<pk>\d+)/$', views.actualizeaza_date_adult, name="actualizeaza_date_adult"),
    url(r'schimb_parola_adult/$', views.schimb_parola_adult, name="schimb_parola_adult"),
    url(r'anunturi_totale_adult/$', views.anunturi_totale_adult, name="anunturi_totale_adult"),
    url(r'pag_anunturi_postate_adult/(?P<pk>\d+)/$', views.pag_anunturi_postate_adult, name="pag_anunturi_postate_adult"),
    url(r'^pag_anunturi_adult/(?P<pk>\d+)/$', views.pag_anunturi_adult, name="pag_anunturi_adult"),
    url(r'^promoveaza-ti_afacerea_sau_serviciul/$', views.promoveazati_afacerea_serviciul, name="promoveazati_afacerea_serviciul"),
    url(r'^promoveaza-ti_afacerea/$', views.promoveazati_afacerea, name="promoveazati_afacerea"),
    url(r'^promoveazati_serviciul/$', views.promoveazati_serviciul, name="promoveazati_serviciul"),
    #####################CATEGORII_ADULT#######################
    url(r'^auto_moto_ambarcatiuni/$', views.auto_adult, name="auto_adult"),
    url(r'^autoturisme/$', views.autoturisme, name="autoturisme"),
    url(r'^ambarcatiuni/$', views.ambarcatiuni, name="ambarcatiuni"),
    url(r'^autoutilitare/$', views.autoutilitare, name="autoutilitare"),
    url(r'^camioane_rulote_remorci/$', views.camioane_rulote_remorci, name="camioane_rulote_remorci"),
    url(r'^motociclete_scutere_atv/$', views.motociclete_scutere_atv, name="motociclete_scutere_atv"),
    url(r'^piese_auto/$', views.piese_auto, name="piese_auto"),
    url(r'^roti_jante_anvelope', views.roti_jante_anvelope, name="roti_jante_anvelope"),
    url(r'^caroserie_interior', views.caroserie_interior, name="caroserie_interior"),
    url(r'^mecanica_electrica/$', views.mecanica_electrica, name="mecanica_electrica"),
    url(r'^agro_si_industrie/$', views.agro_si_industrie, name="agro_si_industrie"),
    url(r'^utilaje_agricole_si_industriale/$', views.utilaje, name="utilaje"),
    url(r'^animale_domestice/$', views.animale_domestice, name="animale"),
    url(r'^produse_piata/$', views.produse_piata, name="produse"),
    url(r'^imobiliare/$', views.imobiliare, name="imobiliare"),
    url(r'^apartamente_de_vanzare/$', views.apartamente_de_vanzare, name="apartamente_de_vanzare"),
    url(r'^apartamente_de_inchiriat/$', views.apartamente_de_inchiriat, name="apartamente_de_inchiriat"),
    url(r'^birouri/$', views.birouri, name="birouri"),
    url(r'^case_de_vanzare/$', views.case_de_vanzare, name="case_de_vanzare"),
    url(r'^case_de_inchiriat/$', views.case_de_inchiriat, name="case_de_inchiriat"),
    url(r'^terenuri_agricole/$', views.terenuri_agricole, name="terenuri_agricole"),
    url(r'^terenuri_constructii/$', views.terenuri_constructii, name="terenuri_constructii"),
    url(r'^spatii_comerciale/$', views.spatii_comerciale, name="spatii_comerciale"),
    url(r'^spatii_industriale/$', views.spatii_industriale, name="spatii_industriale"),
    url(r'^moda/$', views.moda, name="moda"),
    url(r'^haine_dama/$', views.haine_dama, name="haine_dama"),
    url(r'^haine_barbati/$', views.haine_barbati, name="haine_barbati"),
    url(r'^incaltaminte_dama/$', views.incaltaminte_dama, name="incaltaminte_dama"),
    url(r'^incaltaminte_barbati/$', views.incaltaminte_barbati, name="incaltaminte_barbati"),
    url(r'^bijuterii/$', views.bijuterii, name="bijuterii"),
    url(r'^cosmetice/$', views.cosmetice, name="cosmetice"),
    url(r'^accesorii/$', views.accesorii, name="accesorii"),
    url(r'^electronice_si_electrocasnice/$', views.electronice_si_electrocasnice, name="electronice_si_electrocasnice"),
    url(r'^telefoane/$', views.telefoane_adult, name="telefoane"),
    url(r'^tablete/$', views.tablete_adult, name="tablete"),
    url(r'^electrocasnice/$', views.electrocasnice, name="electrocasnice"),
    url(r'^laptop_calculator/$', views.laptop_calculator, name="laptop_calculator"),
    url(r'^aparate_foto/$', views.aparate_foto, name="aparate_foto"),
    url(r'^console/$', views.console, name="console"),
    url(r'^afaceri_servicii/$', views.afaceri_servicii, name="afaceri_servicii"),
    url(r'^cafenele/$', views.cafenele, name="cafenele"),
    url(r'^cofetarii/$', views.cofetarii, name="cofetarii"),
    url(r'^constructii/$', views.constructii, name="constructii"),
    url(r'^cabinete_medicale/$', views.cabinete_medicale, name="cabinete_medicale"),
    url(r'^fast_food/$', views.fast_food, name="fast_food"),
    url(r'^restaurante/$', views.restaurante, name="restaurante"),
    url(r'^contabilitate/$', views.contabilitate, name="contabilitate"),
    url(r'^digital_marketing/$', views.digital_marketing, name="digital_marketing"),
    url(r'^grafic_design/$', views.grafic_design, name="grafic_design"),
    url(r'^meditatii/$', views.meditatii, name="meditatii"),
    url(r'^programare_si_tehnologie/$', views.programare_si_tehnologie, name="programare_si_tehnologie"),
    url(r'^video_si_animatii/$', views.video_si_animatii, name="video_si_animatii"),
    url(r'^animale_de_companie/$', views.animale_de_companie, name="animale_de_companie"),
    url(r'^adoptii/$', views.adoptii_animale, name="adoptii_animale"),
    url(r'^accesorii_animale/$', views.accesorii_animale, name="accesorii_animale"),
    url(r'^locuri_de_munca/$', views.locuri_de_munca, name="locuri_de_munca"),
    url(r'^agenti_de_vanzari/$', views.agenti_vanzari, name="agenti_vanzari"),
    url(r'^confectii_croitori/$', views.confectii, name="confectii"),
    url(r'^cosmeticieni_frizeri/$', views.cosmeticieni, name="cosmeticieni"),
    url(r'^ingineri_meseriasi_constructori/$', views.ingineri, name="ingineri"),
    url(r'^munca_in_strainatate/$', views.munca, name="munca"),
    url(r'^paza_si_protectie/$', views.paza_si_protectie, name="paza_si_protectie"),
    url(r'^personal_hotelier/$', views.personal_hotelier, name="personal_hotelier"),
    url(r'^sport_timp_liber_si_hobby/$', views.sport_timp_liber, name="sport_timp_liber"),
    url(r'^articole_sportive/$', views.articole_sportive_adult, name="articole_sportive_adult"),
    url(r'^carti_filme/$', views.carti_filme, name="carti_filme"),
    url(r'^arta_antichitati/$', views.arta_antichitati, name="arta_antichitati"),
    url(r'^muzica_instrumente_muzicale/$', views.muzica_adult, name="muzica_adult"),
    url(r'^mici_intreprinzatori_autohtoni/$', views.intreprinzatori_autohtoni, name="intreprinzatori_autohtoni"),
    url(r'^matrimoniale/$', views.matrimoniale, name="matrimoniale"),

    url(r'^pag_afaceri/(?P<pk>\d+)/$', views.pag_afaceri, name="pag_afaceri"),
    url(r'^pag_servicii/(?P<pk>\d+)/$', views.pag_servicii, name="pag_servicii"),
]