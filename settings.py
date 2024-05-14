# -*- coding: utf-8 -*-
import json
settings = open('settings.json','w+')
settingsd={}
rel = (int(input("Укажите кол-во рандомных эффектов(ЦЕЛЫМ числом)\n")));vidc = (int(input("Укажите кол-во уникализаций/ролик(ЦЕЛЫМ числом)\n")));mind = (int(input("Укажите минимальную длительность(ЦЕЛЫМ числом)\n")));maxd = (int(input("Укажите максимальную длительность(ЦЕЛЫМ числом)\n")));doMirror = bool(int(input("Включить отзеркаливание(1 - да, 0 - нет)?\n")));showEffect = bool(int(input("Включить эффект появления(1 - да, 0 - нет)?\n")));doRotate = bool(int(input("Включить поворот(1 - да, 0 - нет)?\n")));doblur = bool(int(input("Включить эффект размытия(1 - да, 0 - нет)?\n")));doBlurIn = bool(int(input("Включить эффект вводного размытия(1 - да, 0 - нет)?\n")))
if doblur or doBlurIn:
	blursigma = (int(input("Укажите радиус размытия(в пикселях)\n")))
else:
	blursigma = 0
settingsd['rel']=rel;settingsd['vidc']=vidc;settingsd['mind']=mind;settingsd['maxd']=maxd;settingsd['doMirror']=doMirror;settingsd['showEffect']=showEffect;settingsd['doRotate']=doRotate;settingsd['doblur']=doblur;settingsd['blursigma']=blursigma;settingsd['doBlurIn']=doBlurIn
settings.write(json.dumps(settingsd))
settings.close()
print("Настройки успешно записаны!")