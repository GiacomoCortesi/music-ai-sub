export default function ConverterLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <section className="h-full flex flex-col items-center justify-center gap-4 py-8 md:py-10">
      <div className="h-full inline-block max-w-lg text-center justify-center">
        {children}
      </div>
    </section>
  );
}
