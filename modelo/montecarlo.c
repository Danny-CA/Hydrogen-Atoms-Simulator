#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include<time.h> 
#include "montecarlo.h"
#include "population.h"
#include "people.h"

#define M_PI 3.14159265358979323846

int healthcare(People *k){
  k->time_recovery -= 1.0;
  if ( k->time_recovery <= 0.0){
    k->status = 2; //immune
    k->time_recovery = 0.0;
  }
  return 1;
}


//Elastic Collision implementation
//https://williamecraver.wixsite.com/elastic-equations
int updateTrajectory(People *k, People *m,double radii,double A, double B){
  double v1,v2;
  double v1x,v1y,v2x,v2y,a,b,c,d,x1,y1,x2,y2,phi,theta1,theta2,pi2;
  double epsilon = 1e-10;
  double u,w,mycos1,mysin1;
  double norm, dot_product;
  v1x = k->velocity[0];
  v1y = k->velocity[1];
  v2x = m->velocity[0];
  v2y = m->velocity[1];
  x1 = k->position[0];
  y1 = k->position[1];
  x2 = m->position[0];
  y2 = m->position[1];


  //check border in X: a left and c right
  if (x1 < 0.0){
    if ((A+x1) < radii){
      if(x2 > 0.0){
	if ( (A-x2) < radii){
	  x2 = -2.0*A + x2;
	}
      }
    }
  }

  //check border in X: a right and c left
  if (x1 > 0.0){
    if ((A-x1) < radii){
      if(x2 < 0.0){
	if ( (A+x2) < radii){
	  x1 = -2.0*A + x1;
	}
      }
    }
  }

  //check border in X: a top and c bottom
  if (y1 < 0.0){
    if ((B+y1) < radii){
      if(y2 > 0.0){
	if ( (B-y2) < radii){
	  y2 = -2.0*B+y2;
	}
      }
    }
  }

  //check border in X: a bottom and c top
  if (y1 > 0.0){
    if ((B-y1) < radii){
      if(y2 < 0.0){
	if ( (B+y2) < radii){
	  y1 = -2.0*B+y1;
	}
      }
    }
  }


  
  

  norm = fabsf(pow(x1-x2,2.0)+pow(y1-y2,2.0));
  dot_product = (v1x-v2x)*(x1-x2) + (v1y-v2y)*(y1-y2);
  k->velocity[0] = v1x - (dot_product/norm)*(x1-x2);
  k->velocity[1] = v1y - (dot_product/norm)*(y1-y2);

  norm = fabsf(pow(x2-x1,2.0)+pow(y2-y1,2.0));
  dot_product = (v2x-v1x)*(x2-x1) + (v2y-v1y)*(y2-y1);
  m->velocity[0] = v2x - (dot_product/norm)*(x2-x1);
  m->velocity[1] = v2y - (dot_product/norm)*(y2-y1);


  
//  
//  v1 = sqrt(a*a + b*b);
//  v2 = sqrt(c*c + d*d);
//  //printf("[a,b][c,d][x1,y1][x2,y2]=[%lf,%lf][%lf,%lf][%lf,%lf][%lf,%lf]\n",a,b,c,d,x1,y1,x2,y2);
//  //a close to zero
//  u=y2-y1;
//  w=x2-x1;
//  //printf("b/a d/c u/w = %lf\t%lf\t%lf\n",b/a,d/c,u/w);
//  pi2=M_PI/2.0;
//  theta1=atan(b/a);
//  theta2=atan(d/c);
//  phi=atan(u/w);
//
//  if(fabsf(theta2-phi) <= 1e-2){
//    mycos1= 1.0;
//    mysin1=0.0;
//  }else{
//    mycos1 = fabsf(cos(theta2-phi));
//    mysin1 = fabsf(sin(theta2-phi));
//  }
//  
//  if ((-epsilon <= v1) && (v1 <= epsilon)){    
//    k->velocity[0] = v2*mycos1*cos(phi);
//    k->velocity[1] = v2*mycos1*sin(phi);
//    m->velocity[0] = v2*mysin1*cos(phi+pi2);
//    m->velocity[1] = v2*mysin1*sin(phi+pi2); 
//    return 1;
//  }
//
//  if ((-epsilon <= v2) && (v2 <= epsilon)){    
//    k->velocity[0] = v1*sin(theta1-phi)*cos(phi+pi2);
//    k->velocity[1] = v1*sin(theta1-phi)*sin(phi+pi2);
//    m->velocity[0] = v1*cos(theta1-phi)*cos(phi);
//    m->velocity[1] = v1*cos(theta1-phi)*sin(phi); 
//
//    return 1;
//  }

  

  /*

  
  if ((-epsilon <= a) && (a <= epsilon) && (-epsilon <= b) && (b <= epsilon)){
    theta1= 0.0;
  }else if((0.0 <= a) && (a <= epsilon) && (b > 0.0) ){
    //+\infty
    theta1=3.1416/2.0;
  } else if((0.0 <= a) && (a <= epsilon) && (b < 0.0) ){
    //-\infty
    theta1=-3.1416/2.0;
  }else if((-epsilon <= a) && (a < 0.0) && (b < 0.0) ){
    //-\infty
    theta1=3.1416/2.0;
  }else if((-epsilon <= a) && (a < 0.0) && (b > 0.0) ){
    //-\infty
    theta1=-3.1416/2.0;
  }else{  
    theta1=atan(b/a);
  }


  //a close to zero
  if ((-epsilon <= c) && (c <= epsilon) && (-epsilon <= d) && (d <= epsilon)){
    theta2= 3.1416;
  }else if((0.0 <= c) && (c <= epsilon) && (d > 0.0) ){
    //+\infty
    theta2=3.1416/2.0;
  } else if((0.0 <= c) && (c <= epsilon) && (d < 0.0) ){
    //-\infty
    theta2=-3.1416/2.0;
  }else if((-epsilon <= c) && (c < 0.0) && (d < 0.0) ){
    //-\infty
    theta2=3.1416/2.0;
  }else if((-epsilon <= c) && (c < 0.0) && (d > 0.0) ){
    //-\infty
    theta2=-3.1416/2.0;
  }else{  
    theta2=atan(d/c);
  }

  u=y2-y1;
  w=x2-x1;
  //a close to zero
   if ((-epsilon <= u) && (u <= epsilon) && (-epsilon <= w) && (w <= epsilon)){
     phi= 0.0;
   }else if((0.0 <= w) && (w <= epsilon) && (u > 0.0) ){
    //+\infty
    phi=3.1416/2.0;
  } else if((0.0 <= w) && (w <= epsilon) && (u < 0.0) ){
    //-\infty
    phi=-3.1416/2.0;
  }else if((-epsilon <= w) && (w < 0.0) && (u < 0.0) ){
    //-\infty
    phi=3.1416/2.0;
  }else if((-epsilon <= w) && (w < 0.0) && (u > 0.0) ){
    //-\infty
    phi=-3.1416/2.0;
  }else{  
      phi=atan(u/w);
  }

  */
  
  //  pi2=3.1416/2.0;
    
  //k->velocity[0] = v2*cos(theta2-phi)*cos(phi)+ v1*sin(theta1-phi)*cos(phi+pi2);
  //k->velocity[1] = v2*cos(theta2-phi)*sin(phi)+v1*sin(theta1-phi)*sin(phi+pi2);
  //m->velocity[0] = v1*cos(theta1-phi)*cos(phi)+v2*sin(theta2-phi)*cos(phi+pi2);
  //m->velocity[1] = v1*cos(theta1-phi)*sin(phi)+v2*sin(theta2-phi)*sin(phi+pi2); 

  //printf("INTERACTION  [%lf,%lf][%lf,%lf]\n",k->velocity[0],k->velocity[1],m->velocity[0],m->velocity[1]);
  
  /*
  momentum = m1 + m2;
  //srand(time(0));
  randomNumber= (float)rand() / (float)RAND_MAX ;
  m1 = randomNumber*momentum;
  m2 = momentum - m1;
  //srand(time(0));
  theta = ((float)rand() / (float)RAND_MAX)*3.1416*2.0 ;
  W = cos(theta)*m1;
  Z = sin(theta)*m1;
  k->velocity[0] = W;
  k->velocity[1] = Z;
  //srand(time(0));
  theta = ((float)rand() / (float)RAND_MAX)*3.1416*2.0 ;
  W = cos(theta)*m2;
  Z = sin(theta)*m2;
  m->velocity[0] = W;
  m->velocity[1] = Z; 
  */
  return 1;  
}

//rt = set recovery time
boolean intersection(People *k, People *m,double radii, double rt, double A, double B){
  double a,b,c,d,distance;
  a = k->position[0];
  b = k->position[1];
  c = m->position[0];
  d = m->position[1];

  //check border in X: a left and c right
  if (a < 0.0){
    if ((A+a) < radii){
      if(c > 0.0){
	if ( (A-c) < radii){
	  c = -2.0*A+c;
	}
      }
    }
  }

  //check border in X: a right and c left
  if (a > 0.0){
    if ((A-a) < radii){
      if(c < 0.0){
	if ( (A+c) < radii){
	  a = -2.0*A+a;
	}
      }
    }
  }


  //check border in X: a left and c right
  if (b < 0.0){
    if ((B+b) < radii){
      if(d > 0.0){
	if ( (B-d) < radii){
	  d = -2.0*B+d;
	}
      }
    }
  }

  //check border in X: a right and c left
  if (b > 0.0){
    if ((B-b) < radii){
      if(d < 0.0){
	if ( (B+d) < radii){
	  b = -2.0*B+b;
	}
      }
    }
  }

  

  
  
  //if ( ((A+a) < radii)  && ((A-fabs(c)) < radii)) {
  //    c = a - c;
  //}


  distance = sqrt(pow(c-a,2) + pow(d-b,2));
  if (distance <= radii){
    if(  (k->status==1) && (m->status==0)){
      m->status=1;
      m->time_recovery = rt;
    }else if((k->status==0) && (m->status==1)) {
      k->status=1;
      k->time_recovery = rt;
    }    
    return true;
  }else{
    return false;
  }
}


int interaction(Population *population, double radii, double rt, double A, double B){
  int k,m;
  for(k=0;k< population->iterator;k++){
    //update the position of the people
    for(m=k+1;m < population->iterator;m++){
      //update the position of the people
      if (intersection(&population->people[k],&population->people[m],radii,rt,A,B)){
	//printf("interseciontion! %i,%i\n",k,m);
	updateTrajectory(&population->people[k],&population->people[m],radii,A,B);

      }
    }
  }
  return 1;
}

int integrate(People *people, double dt, double x_A, double x_B, double y_A, double y_B){
  //v = d/dt  ->  d = v*dt
  double d,v;
  //update in X
  v = people->velocity[0];
  d = v*dt;
  people->position[0] += d;
//  //element exit to left side.
//  if (people->position[0] < x_A){  
//    people->position[0] = x_B + (people->position[0] - x_A);
//  }else if ( x_B < people->position[0]){   //element exit to right side.
//    people->position[0] = x_A +  (people->position[0] - x_B);
//  }
  
  //update in Y
  v = people->velocity[1];
  d = v*dt;
  people->position[1] += d;

//    //element exit to top.
//  if (people->position[1] > y_A){  
//    people->position[1] = y_B + (people->position[1] - y_A);
//  } else if ( people->position[1] < y_B ){   //element exit to right side.
//    people->position[1] = y_A +  (people->position[1] - y_B);
//  }
//
  return 1;
}

int fix_borders(People *people, double dt, double x_A, double x_B, double y_A, double y_B){
  //v = d/dt  ->  d = v*dt
  double d,v;
  //update in X

  //element exit to left side.
  if (people->position[0] < x_A){  
    people->position[0] = x_B + (people->position[0] - x_A);
  }else if ( x_B < people->position[0]){   //element exit to right side.
    people->position[0] = x_A +  (people->position[0] - x_B);
  }
  
  //element exit to top.
  if (people->position[1] > y_A){  
    people->position[1] = y_B + (people->position[1] - y_A);
  } else if ( people->position[1] < y_B ){   //element exit to right side.
    people->position[1] = y_A +  (people->position[1] - y_B);
  }

  return 1;
}




MonteCarlo new_MonteCarlo(char name[], Population population, double A, double B){
  MonteCarlo mc;
  sprintf(mc.name,"%s",name);
  mc.population = population;
  mc.steps=0;
  mc.prints=0;
  mc.A = A;
  mc.B = B;
  return mc;
}

int run_MonteCarlo(MonteCarlo mc, int steps, int prints, double radii,double dt,double rt){
  int i=0;
  int j;
  int k;
  //float dt;
  double x_A,x_B,y_A,y_B;
  int healty,sick,immune,dead;
  
  x_A = -mc.A/2;
  x_B = mc.A/2;
  y_A = mc.B/2;
  y_B = -mc.B/2;

  
  //dt=1.0;
  
  j=0;

  //printing step 0
  //printf("iteration %i\n",i);
  //for(k=0;k< mc.population.iterator;k++){
  //  print_People(mc.population.people[k]);
  //}

            healty=0;
      sick=0;
      immune=0;
      dead=0;
      for(k=0;k< mc.population.iterator;k++){
	switch(mc.population.people[k].status){
	case 0:
	  healty++;
	  break;
	case 1:
	  sick++;
	  break;
	case 2:
	  immune++;
	  break;
	case -1:
	  dead++;
	  break;
	default:
	  printf("Warnning: no status recognized!\n");
	}
	  
      }
      printf("#%i\t%i\t%i\t%i\t%i\n",0,healty,sick,immune,dead);
      for(k=0;k< mc.population.iterator;k++){
	print_People(mc.population.people[k]);
      }

  
  for(i=0;i<steps;i++){
    //Montecarlo integration
    //the last two parameters are the half of the region (optimize)


    interaction( &mc.population, radii,rt,x_B,y_A);

    
    for(k=0;k< mc.population.iterator;k++){
      //update the position of the people
      integrate( &mc.population.people[k],dt,x_A,x_B,y_A,y_B);
      //check if is sick
      if (mc.population.people[k].status == 1){
	healthcare(&mc.population.people[k]);
      }	
    }

    for(k=0;k< mc.population.iterator;k++){
      fix_borders( &mc.population.people[k],dt,x_A,x_B,y_A,y_B);
    }

    
    //for(k=0;k< mc.population.iterator;k++){
      //update the position of the people
      //}
    
    j++;
    if (j == prints){

      //count status of the people
      healty=0;
      sick=0;
      immune=0;
      dead=0;
      for(k=0;k< mc.population.iterator;k++){
	switch(mc.population.people[k].status){
	case 0:
	  healty++;
	  break;
	case 1:
	  sick++;
	  break;
	case 2:
	  immune++;
	  break;
	case -1:
	  dead++;
	  break;
	default:
	  printf("Warnning: no status recognized!\n");
	}
	  
      }
      printf("#%i\t%i\t%i\t%i\t%i\n",i+1,healty,sick,immune,dead);
      for(k=0;k< mc.population.iterator;k++){
	print_People(mc.population.people[k]);
      }
      j=0;
    }    
  }

  
  return 1;
}

