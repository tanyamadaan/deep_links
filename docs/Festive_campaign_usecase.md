## Use Case: Festival Collection Curation with Beckn Deep Links

During festive seasons like Diwali, buyer apps can enhance the shopping experience by curating special collections and offers tailored to the festive spirit. These curated collections can be showcased directly to users through dynamic landing pages, providing a seamless and engaging experience for buyers. By leveraging Beckn deep links, buyer apps can redirect users to specific collections, enhancing discoverability and driving traffic to curated offers.

### 1. Curated Festival Collection Landing Pages

Buyer apps can create exclusive landing pages showcasing Diwali collections or other festive offers, providing users with a convenient way to explore relevant products and services. For instance, when a user clicks on a specially designed link or scans a QR code related to a festival collection, they are instantly redirected to a curated landing page within the buyer app that highlights Diwali offers.

**Deep Link Structure:**  

```
beckn://ondc?message.intent.tags.descriptor.code=collection_details&message.intent.tags.list.descriptor.code=collection_name&message.intent.tags.list.value=diwali&message.intent.tags.list.descriptor.code=valid_from&message.intent.tags.list.value=2024-10-28T00:00:00.000Z&message.intent.tags.list.descriptor.code=valid_to&message.intent.tags.list.value=2024-11-04T00:00:00.000Z&source_id=b00599c4-a26d-4094-b7d2-2b1076c23a18
```

When a buyer interacts with this link, the system automatically identifies and launches a compatible buyer app that supports the Beckn protocol. The app reads the parameters from the deep link, identifies the context as a festival collection, and directly redirects the user to a specific landing page (curated by the buyer app) based on the collection name received in the deep link. This allows users to explore time-sensitive offers and products tailored to the festive period.

#### Key Features:

    **Curated Experience:** Buyers are presented with a specially designed landing page that captures the essence of the festival, showcasing offers, discounts, and exclusive products.
    **Seamless Navigation:** Users can effortlessly access the collection through deep links, enhancing their shopping journey by eliminating the need to manually search for festive products.
    **Time-Bound Offers:** The link includes details like the validity of the offers, ensuring that users are aware of the limited-time nature of the deals, driving urgency and action.