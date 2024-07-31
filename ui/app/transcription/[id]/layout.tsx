export default function TrasncriptionLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <section className="flex flex-col items-center justify-center gap-4 py-8 ">
      <div className="w-11/12 inline-block text-center justify-center">
        {children}
      </div>
    </section>
  );
}
