/*
	Programmer: Jevin Evans
	Date: 7/19/2019
	Program: Equipment Class
	Description: The Equipment class allows for creation of objects in the game to be used by characters and placed inside of the armor or in other holders/storage containers inside of the game 
 */

#ifndef STATS_H
#define STATS_H

#include <iostream>
// #include <fstream>
#include <string>
using namespace std;

class Stats
{
	private:
		int hp_now;
        int hp_max;
        int mp_now;
        int mp_max;
        int strength;
        int speed;
        int intel;
	
	public:
        Stats()
        {
            this->hp_max = 0;
            this->hp_now = 0;
            this->mp_max = 0;
            this->mp_now = 0;
            this->strength = 0;
            this->speed = 0;
            this->intel = 0;
        }

        Stats(int hn, int hm, int mn, int mm, int str, int spd, int intel)
        {
            this->hp_max = hn;
            this->hp_now = hm;
            this->mp_max = mn;
            this->mp_now = mm;
            this->strength = str;
            this->speed = spd;
            this->intel = intel;
        }

        Stats(Stats* s)
        {
            this->hp_max = s->hp_max;
            this->hp_now = s->hp_now;
            this->mp_max = s->mp_max;
            this->mp_now = s->mp_now;
            this->strength = s->strength;
            this->speed = s->speed;
            this->intel = s->intel;
        }

        //Level UP
        void levelup(double percentage)
        {
            while(percentage > 1)
            {
                percentage /= 10;
            }

            percentage += 1;

            // this->getHPMAX           

        }

        //HEAL/RESTORE
        void heal(double percentage)
        {
            if
        }

        //PRINT
        void PRINT()
        {

        }

        // Setters
        void setHPMAX(int h){this->hp_max = h;}
        void setHPNOW(int h){this->hp_now = h;}
        void setMPMAX(int m){this->mp_max = m;}
        void setMPNOW(int m){this->mp_now = m;}
        void setStrength(int s){this->strength = s;}
        void setSpeed(int s){this->speed = s;}
        void setIntel(int i){this->intel = i;}

        // Getters
        int getHPMAX(){return this->hp_max;}
        int getHPNOW(){return this->hp_now;}
        int getMPMAX(){return this->mp_max;}
        int getMPNOW(){return this->mp_now;}
        int getStrength(){return this->strength;}
        int getSpeed(){return this->speed;}
        int getIntel(){return this->intel;}

};


#endif