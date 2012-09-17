package no.gombos.ai.robocode.task1;

import robocode.*;

public class ReflexBot extends Robot {

	int count;
	double turnAmt;
	
	public void run(){
		
		count = 0;
		// amount to turn
		turnAmt = 10;
		// keep gun the same direction 
		setAdjustGunForRobotTurn(true);
		
		while(true){
			turnGunRight(turnAmt);
			
			// add for how long we've looked for a robot
			count++;
			// turns the arm different ways if it cannot find a robot at once
			if(count > 2){
				turnAmt = -10;
			}
			if(count > 5){
				turnAmt = 10;
			}
			
		}
	}
	
	public void onScannedRobot(ScannedRobotEvent e){
		// we found a robot, resets count
		turnAmt=0;
		count = 0;
		
		// fire at it!!!
		fire(3);
		
		// walk a bit around it
		if(e.getDistance() > 150){
			if(this.getHeading() != this.getGunHeading()){
				turnLeft(15);
			}
			ahead(40);
		}
		
	}
	
	public void onHitByBullet(HitByBulletEvent e){
		// start to drive if we're standing still, stop in the reverse case
		if(getVelocity() != 0){
			ahead(40);
		} else
			stop();
	}
	
	
	public void onHitRobot(HitRobotEvent e){
		// start to drive if we're standing still, stop in the reverse case
		if(getVelocity() != 0){
			ahead(40);
		} else
			stop();
	}
}
