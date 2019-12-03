#include <iostream>
#include <sstream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

using namespace std;

using VS = vector< string >;

class KnotHash {
public:
    using Collection = vector< int >;
    string hash64( const string& input, int N=256, int pos=0, unsigned char len=0, int skip=0, string ans={} ){
        Collection cur( N ), L; // (cur)rent list, (L)engths
        generate( cur.begin(), cur.end(), [i=0]() mutable { return i++; });
        istringstream stream{ input };
        using Iter = istream_iterator< unsigned char >;
        copy( Iter( stream ), Iter(), back_inserter( L ));
        L.insert( L.end(), { 17, 31, 73, 47, 23 });
        for( auto round{ 64 }; round--; )
            for( auto len: L )
                knot( cur, pos, len, skip );
        for( auto chunk{ 0 }; chunk < 16; ++chunk ){
            auto begin = chunk * 16;
            auto x = cur[ begin ];
            for( auto i{ begin+1 }; i < begin + 16; x ^= cur[ i++ ] );
            ostringstream stream;
            stream << setw( 2 ) << setfill( '0' ) << hex << x;
            ans.append( stream.str() );
        }
        return ans;
    }
private:
    void knot( Collection& cur, int& pos, int len, int& skip ){
        const auto N = cur.size();
        auto next{ cur };
        for( auto i{ 0 }; i < len; ++i ){
            auto p = ( pos + i ) % N,
                 q = ( pos + len - i - 1 ) % N;
            if( p < 0 ) p += len;
            if( q < 0 ) q += len;
            next[ q ] = cur[ p ];
        }
        swap( cur, next );
        pos += ( len + skip ) % N;
        ++skip;
    }
};

class DisjointSet {
public:
    using PII = pair< int,int >;
    DisjointSet( int N ){
        for( auto i{ 0 }; i < N; ++i ){
            for( auto j{ 0 }; j < N; ++j ){
                auto key = getKey({ i,j });
                P.insert({ key, key });
            }
        }
    }
    void Union( PII a, PII b ){
        auto pa = Find( a.first, a.second ),
             pb = Find( b.first, b.second );
        P[ pa ] = pb; // arbitrary choice
    }
    string Find( int i, int j ){
        auto key = getKey({ i,j });
        return Find( key );
    }
    string Find( const string& key ){
        if( key == P[ key ] )
            return P[ key ];
        return P[ key ] = Find( P[ key ] );
    }
    using Unique = unordered_set< string >;
    int Count( VS& A, Unique U={} ){
        return count_if( P.begin(), P.end(), [&]( auto pair ){
            auto key = pair.first;
            auto[ i,j ] = getPair( key );
            return A[ i ][ j ] == '1' && U.insert( Find( key ) ).second;
        });
    }
private:
    unordered_map< string,string > P;
    string getKey( PII x ){
        stringstream ss;
        ss << x.first << "," << x.second;
        return ss.str();
    }
    PII getPair( const string& key ){
        istringstream is{ key };
        char _;
        auto i{ 0 }, j{ 0 };
        is >> i >> _ >> j;
        return{ i,j };
    }
};

class Solution {
public:
    using Result = pair< int,int >;
    Result defrag( const string& key, int N=128, KnotHash hasher={}, VS A={}, int bits=0, int regions=0 ){
        for( auto i{ 0 }; i < N; ++i ){
            ostringstream os;
            os << key << "-" << i;
            auto hash = hasher.hash64( os.str() );
            auto[ cnt, set ] = getBits( hash );
            bits += cnt;
            A.emplace_back( set );
        }
        DisjointSet S( N );
        dfs( A, S, N );
        return{ bits, S.Count( A ) };
    }
private:
    using BitInfo = pair< int,string >;
    using BitSet = bitset< 4 >;
    BitInfo getBits(const string &hash, int cnt=0, string set={} ){
        size_t num{ 0 };
        for( auto c: hash ){
            stringstream ss;
            ss << hex << c;
            ss >> num;
            cnt += __builtin_popcount( num );
            BitSet bs{ num };
            set.append( bs.to_string() );
        }
        return{ cnt, set };
    }
    using PII = pair< int,int >;
    struct Hash {
        size_t operator()( const PII& pair ) const {
            return 128 * pair.first + pair.second;
        }
    };
    using VPII = vector< PII >;
    using Seen = unordered_set< PII, Hash >;
    VPII directions{ { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    void dfs( const VS& A, DisjointSet& S, int N, Seen seen={} ){
        for( auto i{ 0 }; i < N; ++i )
            for( auto j{ 0 }; j < N; ++j )
                go( A, S, N, i, j, seen );
    }
    void go( const VS& A, DisjointSet& S, int N, int i, int j, Seen& seen ){
        if( A[ i ][ j ] == '0' || ! seen.insert({ i,j }).second )
            return;
        auto p = S.Find( i, j );
        for( auto d: directions ){
            auto u = i + d.first,
                 v = j + d.second;
            if( 0 <= u && u < N && 0 <= v && v < N && A[ u ][ v ] == '1' ){
                S.Union( { i,j }, { u,v } );
                go( A, S, N, u, v, seen );
            }
        }
    }
};

int main() {
    Solution solution;
    auto[ bits, regions ] = solution.defrag( "uugsqrei" );
    cout << "Part 1: " << bits << endl
         << "Part 2: " << regions << endl;
    return 0;
}
