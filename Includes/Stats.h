/*
	Programmer: Jevin Evans
	Date: 7/19/2019
	Program: Equipment Class
	Description: The Equipment class allows for creation of objects in the game to be used by characters and placed inside of the armor or in other holders/storage containers inside of the game 
 */

// http://howtomakeanrpg.com/a/how-to-make-an-rpg-stats.html

#ifndef STATS_H
#define STATS_H

#include <iostream>
#include <fstream>
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

        Stats(int hm, int mm, int str, int spd, int intel)
        {
            this->hp_max = hm;
            this->hp_now = hm;
            this->mp_max = mm;
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
            if(percentage == 100)
            {
                percentage = 1;
            }
            else
            {
                while(percentage > 1)
                {
                    percentage /= 10;
                }
            }
            
            percentage += 1;

            this->hp_max *= percentage;
            this->hp_now = this->hp_max;
            this->mp_max *= percentage;
            this->mp_now = this->mp_max;
            this->strength *= percentage;
            this->speed *= percentage;
            this->intel *= percentage;
        }

        //Stats Actions and Uses
        void damage(double cost, bool percentage)
        {
            if(percentage)
            {
                while(cost > 1)
                {
                    cost /= 10;
                }

                this->hp_now = this->hp_now - this->hp_now*cost;
            }
            else
            {
                this->hp_now -= cost;
            }

            if(this->hp_now < 0)
                this->hp_now = 0;
        }

        void heal(double cost, bool percentage)
        {
            if(percentage)
            {
                if(cost == 100)
                    this->hp_now = this->hp_max;
                else
                {
                    while(cost > 1)
                    {
                        cost /= 10;
                    }
                    cost += 1;
                    this->hp_now *= cost;
                }
            }
            else
            {
                this->hp_now += cost;
            }

            if(this->hp_now > this->hp_max)
                this->hp_now = this->hp_max;            
        }

        void mpUse(double cost, bool percentage)
        {
             if(percentage)
            {
                while(cost > 1)
                {
                    cost /= 10;
                }

                this->mp_now = this->mp_now - this->mp_now*cost;
            }
            else
            {
                this->mp_now -= cost;
            }

            if(this->mp_now < 0)
                this->mp_now = 0;
        }
        void mpRestore(double cost, bool percentage)
        {
             if(percentage)
            {
                if(cost == 100)
                    this->mp_now = this->mp_max;
                else
                {
                    while(cost > 1)
                    {
                        cost /= 10;
                    }
                    cost += 1;
                    this->mp_now *= cost;
                }
            }
            else
            {
                this->mp_now += cost;
            }

            if(this->mp_now > this->mp_max)
                this->mp_now = this->mp_max;    
        }

        //PRINT
        void PRINT()
        {
            cout << "HP: " << this->getHPNOW() << "/" << this->getHPMAX() << endl;  
            cout << "MP: " << this->getMPNOW() << "/" << this->getMPMAX() << endl;
            cout << "STR: " << this->getStrength() << "\nSPD: " << this->getSpeed() << "\nINT: " << this->getIntel(); 
            cout << endl << endl;
        }

        int* getAllStats()
        {
            int* array = new int[7];
            array[0] = this->hp_max; 
            array[1] = this->hp_now;
            array[2] = this->mp_max;
            array[3] = this->mp_now;
            array[4] = this->strength; 
            array[5] = this->speed;
            array[6] = this->intel;
            return array;
        }

        void addStats(Stats* other)
        {
            this->hp_max += other->hp_max;
            this->hp_now += other->hp_now;
            this->mp_max += other->mp_max;
            this->mp_now += other->mp_now;
            this->strength += other->strength;
            this->speed += other->speed;
            this->intel += other->intel;
        }

        void removeStats(Stats* other)
        {
            this->hp_max -= other->hp_max;
            this->hp_now -= other->hp_now;
            this->mp_max -= other->mp_max;
            this->mp_now -= other->mp_now;
            this->strength -= other->strength;
            this->speed -= other->speed;
            this->intel -= other->intel;
        }

        void printToFile(ofstream &File)
        {
            cout << "Printing Stats";
            File << this->hp_max << ",";
            File << this->hp_now << ",";
            cout << ".";
            File << this->mp_max << ",";
            File << this->mp_now << ",";
            cout << ".";
            File << this->strength << ",";
            File << this->speed << ",";
            File << this->intel  << ";";
            cout << ".";
            cout << "Done" << endl;
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