from pybnb.pyomo.misc import mpi_partition

from ..common import mpi_available
from runtests.mpi import MPITest

import numpy

def _test_mpi_partition(comm):
    test_ranks = [0]
    if comm is not None:
        import mpi4py.MPI
        test_ranks = list(range(comm.size))
    for x in ([],
              ['a'],
              ['a','b'],
              ['a','b','c'],
              ['a','b','c']*2,
              ['a','b','c']*4,
              ['a','b','c']*16,
              ['a','b','c']*32):
        for root in test_ranks:
            x_accessed_local = numpy.zeros(len(x),
                                           dtype=int)
            for i, xi in mpi_partition(comm,
                                       list(enumerate(x)),
                                       root=root):
                assert x[i] == xi
                x_accessed_local[i] += 1
            x_accessed = numpy.zeros(len(x),
                                     dtype=int)
            if comm is not None:
                comm.Allreduce([x_accessed_local,
                                mpi4py.MPI.INT],
                               [x_accessed,
                                mpi4py.MPI.INT],
                               op=mpi4py.MPI.SUM)
                comm.Barrier()
            else:
                x_accessed[:] = x_accessed_local[:]
            assert (x_accessed == 1).all()

def test_mpi_partition_no_comm():
    _test_mpi_partition(None)

if mpi_available:

    @MPITest(commsize=[1, 2, 4])
    def test_mpi_partition(comm):
        _test_mpi_partition(comm)
