import numpy
import multiprocessing
import argparse
import time

def sample_N_points(args):
	#Pick N random points in a 2x2 square, report how many are inside a circle of radius 1
	N = args[0]
	#Each process should use a different seed for the random number generator
	numpy.random.seed(args[1])
	M=0
	for i in range(0,N):
		x = 2*numpy.random.rand()-1.
		y = 2*numpy.random.rand()-1.
		#Is the point inside the circle?
		if(x**2+y**2 < 1):
			M += 1
	return M

def main():
	#Parse command line arguments to get the number of samples taken per processor
	parser = argparse.ArgumentParser()
	parser.add_argument("N", help="Number of samples per process", type=int)
	parser.add_argument("P", help="Number of processes", type=int)
	args = parser.parse_args()
	N = args.N
	P = args.P

	#Exact value of pi for comparison
	print("Exact pi="+str(numpy.pi))
	#Run the samples, get the number of points inside the circle
	pool = multiprocessing.Pool(processes=P)
	print("Number of CPUs = "+str(multiprocessing.cpu_count()))
	seed_time = int(time.time())
	pool_args = [[N, (i+1)*seed_time] for i in range(0,P)]
	Ms=pool.map(sample_N_points, pool_args)
	M = sum(Ms)
	#Calculate the Monte Carlo value of pi
	print("Approx pi="+str(4.*M/(P*N)))
	print("Diff = "+str(abs(numpy.pi - 4.*M/(P*N))))
	print("Counts from each process = ",Ms)
	print("Using "+str(N)+" samples per process, and a total of "+str(N*P)+" samples over "+str(P)+" processes.")

if __name__=="__main__":
	main()
