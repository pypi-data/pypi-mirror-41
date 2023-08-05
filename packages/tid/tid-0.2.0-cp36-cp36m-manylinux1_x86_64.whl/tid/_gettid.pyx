# https://stackoverflow.com/a/50202496/1698058
cdef extern from "<sys/syscall.h>" nogil:
    int __NR_gettid
    long syscall(long number, ...)


def gettid():
    """Get the LWP id as visible in top/ps.

    Returns:
        long thread id
    """
    return syscall(__NR_gettid)
