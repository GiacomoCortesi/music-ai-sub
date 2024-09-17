/** @type {import('next').NextConfig} */
const nextConfig = {
  async redirects() {
    return [
      {
        source: "/",
        destination: "/converter",
        permanent: true, // Set to true for a permanent redirect (308), or false for a temporary redirect (307)
      },
    ];
  },
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
};

module.exports = nextConfig;
