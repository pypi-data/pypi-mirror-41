# Defines a class instantiating a transmitting civilisation
# Class built assuming transmission via electromagnetic radiation

###############
# Attributes:
###############


# Inherited from agent.py:

# self.pos - position (Vector3D)
# self.vel - velocity (Vector3D)
# self.starpos - host star position (Vector3D)
# self.mstar - host star mass
# self.a - semimajor axis of orbit around host star
# self.meananom - mean anomaly

# self.nu - central frequency of broadcast  (default = HI (1.42 GHz)
# self.bandwidth - bandwidth of broadcast   (default = 1% of 1.42 GHz)
# self.openingangle - opening angle of broadcast
# self.solidangle - solid angle of broadcast  (default = 4pi, i.e. isotropic
# self.n - direction vector of broadcast (Vector3D)

# self.power - broadcast power                  (default = ?)
# self.eirp - effective isotropic radiated power
# self.polarisation - broadcast polarisation
# self.tbegin - broadcast beginning time
# self.tend - broadcast end time
# self.pulseduration - pulse duration (if 0, does not transmit)
# self.pulseinterval - pulse interval (if 0, continuous)


###########
# Methods:
###########

# Inherited/Extended from agent.py

# define_strategy(strategy) - define strategy of Agent
# update(time,dt) - update agent position, velocity and direction vector
# orbit(time) - move agent in orbit around host star
# sample_random(seed,xmin,xmax,ymin,ymax,zmin,zmax,vdisp) - sample position and velocity in uniform cube
# sample_random_sphere(seed, rmin,rmax,vdisp,flatsphere) - sample position and velocity in uniform sphere
# sample_GHZ(seed,inner_radius, outer_radius, scale_length, max_inclination) - sample position and velocity in Galactic Habitable Zone


# transmitted_flux(distance) - compute the flux of radiation from transmitter at a given distance
# broadcast(time,dt) - determine if transmitter is broadcasting at a specific time
# calc_eirp - calculate effective isotropic radiated power
# broadcast(time,dt) - determine if transmitter is transmitting

from numpy import pi,mod,arctan2, power
from taktent.agents.agent import Agent as Parent
from taktent.agents.vector import Vector3D
from taktent.constants import *


class Transmitter(Parent):

    def __init__(self,counter=None,position=zero_vector, velocity=zero_vector, strategy=None, direction_vector=zero_vector, openangle=twopi, starposition=zero_vector, starvelocity=zero_vector,starmass=1.0, semimajoraxis=1.0, inclination=0.0, longascend = 0.0, mean_anomaly=0.0,  nu=1.420e9,bandwidth=1.420e7, solidangle=fourpi, power=None, polarisation=None, tbegin=0.0, tend=0.0, pulseduration=0.0,pulseinterval=0.0, decaylaw=2):
        """
        Initialises a Transmitter object
            
        Keyword Arguments:
        -----------------
        
        counter -- iterator to keep track of object IDs between runs
        position -- cartesian position vector (pc)
        velocity -- cartesian velocity vector (pc yr^-1)
        strategy -- Strategy object defining Agent's pointing behaviour
        direction_vector -- unit vector defining pointing direction of Agent
        openingangle -- opening angle of beam defined by Agent's pointing (radians)
        starposition -- cartesian position vector of host star (pc)
        starvelocity -- cartesian velocity vector of host star (pc yr^-1)
        starmass -- host star mass (solar masses)
        semimajoraxis -- semimajor axis of orbit about host star (AU)
        inclination -- inclination of orbit about host star (radians)
        longascend -- longitude of the ascending node of orbit about host star (radians)
        mean_anomaly -- mean anomaly of orbit about host star (radians)
        
        nu -- central frequency of transmission (Hz)
        bandwidth -- bandwidth of transmission (Hz)
        solidangle -- solid angle of transmission (radians)
        power -- broadcast power (W)
        polarisation -- signal polarisation (not currently used)
        
        tbegin -- time at which broadcasting begins (years)
        tend -- time at which broadcasting ends (years)
        
        pulseduration -- Length of signal pulses (years)
        pulseinterval -- Time interval between pulses (years, set to zero or None for continuous broadcast)
        
        
        Other defined attributes
        ------------------------
        
        eirp - effective isotropic radiated power
        decaylaw - index of radiation decay (1/r^2 for EM, 1/r for GW etc)
        broadcastspeed - transmission speed of broadcast (default is lightspeed) (units: pc yr-1)
        
        detected -- dictionary tracking which observers have detected it
        """
        
        
        Parent.__init__(self,counter, position, velocity, strategy, direction_vector, openangle, starposition, starvelocity,starmass, semimajoraxis, inclination,longascend, mean_anomaly)
        
        self.type="Transmitter"
        self.success_colour = "green"
        self.fail_colour = "gray"
        
        self.nu = nu
        self.bandwidth = bandwidth
        self.solidangle = solidangle
        self.power = power
        self.polarisation = polarisation
        self.tbegin = tbegin
        self.tend = tend
        self.pulseduration = pulseduration
        self.pulseinterval = pulseinterval
        
        self.broadcastspeed = c_pc_yr # assume transmissions move at lightspeed by default
        self.decaylaw = decaylaw # inverse square law of radiation decay by default
        
        # opening angle = fraction of solid angle (opening angle = pi if solid angle = 4 pi)
        self.openingangle = 0.25*self.solidangle
        
        self.detected ={} # dictionary tracking detections
        
        self.calc_eirp()
    
    
    def __str__(self):
        """
        Prints Transmitter data to a string
        
        Returns:
        --------
        Multi-line string containing Transmitter data
        """
        
        return "Transmitter: ID %s: position %f %f %f pointing %f %f %f \n nu %f bandwidth %f power %f openingangle %f pulseduration %f pulseinterval %f"% (self.ID, self.position.x, self.position.y, self.position.z,self.n.x, self.n.y,self.n.z, self.nu, self.bandwidth, self.power,self.openingangle, self.pulseduration, self.pulseinterval)
       
        return s
            
            
    def write_to_file(self):
        """
        Returns a string suitable for writing data to file
        
        Returns:
        --------
        One-line string containing Transmitter data
        """
        return "Transmitter %s %f %f %f   %f %f %f   %f %f %f %f %f %f \n"%(self.ID, self.position.x, self.position.y, self.position.z, self.n.x, self.n.y,self.n.z, self.nu, self.bandwidth, self.power, self.openingangle,self.pulseduration, self.pulseinterval)

    def update(self,time,dt):
        """
        Update position, velocity and direction vector of Transmitter (and broadcast status)
            
        Keyword Arguments:
        ------------------
        time -- current time (years)
        dt -- timestep (years)
            
        """
        
        Parent.update(self,time,dt)
        # check if currently broadcasting (from Transmitter's point of view)
        self.active = self.broadcast(time,dt)

    def calc_eirp(self):
        """Calculate effective isotropic radiated power"""

        self.eirp = self.power*(fourpi)/self.solidangle
    
    
    def transmitted_flux(self,distance):
        """
        Given a distance, computes the flux received at a given location
        
        Keyword Arguments:
        ------------------
        distance - distance between transmitter and location
        
        Returns:
        --------
        Flux
        """
    
        return self.eirp/(fourpi*power(distance*pc,self.decaylaw))

    def broadcast(self,time,dt):
        """
        Is transmitter broadcasting or not?
        
        Keyword Arguments:
        ------------------
        time -- time (years)
        dt -- timestep (years)
        
        Returns:
        --------
        broadcasting -- Is transmitter broadcasting? (boolean)
            
        """

        broadcasting = False
        
        # Check if broadcast not yet begun, or broadcast ended
        if((time<self.tbegin and self.tbegin!=None) or (time > self.tend and self.tend!=None)):
            return broadcasting
        
        # If not pulsing, and within time limits, definitely broadcasting
        if(self.pulseinterval==None or self.pulseinterval==0.0):
            broadcasting=True
        else:
            # period of pulse = pulse duration + pulse interval
            period = self.pulseduration + self.pulseinterval

            # How many pulse cycles have elapsed (real value)
            nperiods = abs(time-self.tbegin)/period
        
            # fraction of time pulse is on during a cycle
            onfrac = self.pulseduration/period

            # Pulse is on if remainder of nperiods is less than onfrac
            broadcasting = mod(nperiods,1.0) < onfrac

        return broadcasting


    def set_colour(self):
    
        if True in self.detected.values():
            self.colour = self.success_colour
        else:
            self.colour = self.fail_colour
