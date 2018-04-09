class Sol811 {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> mapping = new HashMap<>();
        for (String countWeb : cpdomains) {
            String[] parts = countWeb.split(" ");
            int count = Integer.parseInt(parts[0]);
            String web = parts[1];
            int i = -1;
            do {
                String sub = web.substring(i + 1);
                mapping.put(sub, mapping.getOrDefault(sub, 0) + count);
                i = web.indexOf('.', i + 1);
            } while (i != -1);
        }
        List<String> reversedMapping = mapping.entrySet().stream().map(e -> e.getValue() + " " + e.getKey()).collect(Collectors.toList());
        return reversedMapping;
    }
}