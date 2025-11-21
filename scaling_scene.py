from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

class ScalingSystemArchitecture(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Introduction
        self.introduction()
        
        # Chapter 1: Single Server Setup
        self.single_server_setup()
        
        # Chapter 2: Separating Web and Database
        self.separating_web_and_database()
        
        # Chapter 3: Vertical vs Horizontal Scaling
        self.vertical_vs_horizontal_scaling()
        
        # Chapter 4: Load Balancer
        self.load_balancer()
        
        # Chapter 5: Database Replication
        self.database_replication()
        
        # Chapter 6: Cache Layer
        self.cache_layer()
        
        # Chapter 7: CDN
        self.cdn_explanation()
        
        # Chapter 8: Stateless Web Tier
        self.stateless_web_tier()
        
        # Chapter 9: Multiple Data Centers
        self.multiple_data_centers()
        
        # Chapter 10: Message Queue
        self.message_queue()
        
        # Chapter 11: Logging, Metrics, Automation
        self.logging_metrics_automation()
        
        # Chapter 12: Database Sharding
        self.database_sharding()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to Scaling System Architecture from Zero to Millions of Users. Designing a system that supports millions of users is challenging. It's a journey that requires continuous refinement and endless improvement.") as tracker:
            title = Text("Scaling from Zero to", font_size=48, color=BLUE, weight=BOLD)
            subtitle = Text("Millions of Users", font_size=52, color=ORANGE, weight=BOLD)
            title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
            
            self.play(Write(title), run_time=1.5)
            self.play(Write(subtitle), run_time=1.5)
            self.wait(1)
        
        with self.voiceover(text="Today, we'll build a system starting from a single user and gradually scale it to support millions of concurrent users. Let's begin this exciting journey!") as tracker:
            journey_text = Text("The Journey:", font_size=36, color=GREEN)
            journey_text.move_to(UP * 2)
            
            step1 = Text("• Single Server", font_size=28)
            step2 = Text("• Distributed System", font_size=28)
            step3 = Text("• Global Scale", font_size=28)
            
            steps = VGroup(step1, step2, step3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
            steps.next_to(journey_text, DOWN, buff=0.5)
            
            self.play(FadeOut(title_group))
            self.play(Write(journey_text))
            self.play(Write(step1))
            self.wait(0.5)
            self.play(Write(step2))
            self.wait(0.5)
            self.play(Write(step3))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def single_server_setup(self):
        with self.voiceover(text="Chapter One: Single Server Setup. Let's start with the simplest possible architecture. In the beginning, everything runs on one server: the web application, the database, and the cache. This is where every system begins.") as tracker:
            chapter_title = Text("Chapter 1: Single Server Setup", font_size=40, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="Here's how it works. A user types www dot mysite dot com into their browser. First, the domain name system, or DNS, resolves this domain name to an IP address.") as tracker:
            # Create user with devices
            user = self.create_user_icon().shift(LEFT * 5 + UP * 2)
            browser_label = Text("Web Browser", font_size=20).next_to(user, DOWN, buff=0.2)
            
            # DNS Server
            dns_box = Rectangle(height=1.2, width=2, color=PURPLE, fill_opacity=0.3)
            dns_text = Text("DNS", font_size=24, color=PURPLE).move_to(dns_box.get_center())
            dns_group = VGroup(dns_box, dns_text).shift(UP * 2)
            dns_label = Text("Domain Name System", font_size=18).next_to(dns_group, DOWN, buff=0.2)
            
            # Web Server
            server = self.create_server_icon().shift(RIGHT * 4)
            server_label = Text("Web Server", font_size=24).next_to(server, UP, buff=0.3)
            
            self.play(FadeIn(user), Write(browser_label))
            self.play(FadeIn(dns_group), Write(dns_label))
            self.play(FadeIn(server), Write(server_label))
        
        with self.voiceover(text="The DNS server returns the IP address, for example, 15.125.23.214. Now the user's browser knows exactly where to send the request.") as tracker:
            # Show DNS query
            query_arrow = Arrow(user.get_right(), dns_group.get_left(), color=YELLOW, buff=0.2)
            query_text = Text("www.mysite.com?", font_size=18, color=YELLOW).next_to(query_arrow, UP, buff=0.1)
            
            self.play(Create(query_arrow), Write(query_text))
            self.wait(0.5)
            
            # DNS response
            ip_address = Text("15.125.23.214", font_size=20, color=GREEN).next_to(dns_group, RIGHT, buff=1)
            response_arrow = Arrow(dns_group.get_bottom(), ip_address.get_top(), color=GREEN, buff=0.2)
            
            self.play(Create(response_arrow), Write(ip_address))
            self.wait(1)
        
        with self.voiceover(text="The browser then sends an HTTP request directly to the web server at that IP address. The server processes the request and returns either HTML pages for the website or JSON data for API calls.") as tracker:
            # HTTP Request
            self.play(FadeOut(query_arrow), FadeOut(query_text), FadeOut(response_arrow), FadeOut(ip_address))
            
            http_arrow = Arrow(user.get_right() + DOWN * 0.5, server.get_left(), color=BLUE, buff=0.3)
            http_text = Text("HTTP Request", font_size=18, color=BLUE).next_to(http_arrow, DOWN, buff=0.1)
            
            self.play(Create(http_arrow), Write(http_text))
            self.wait(0.5)
            
            # Server components
            components = Text("Web App + Database + Cache", font_size=16, color=ORANGE)
            components.next_to(server, DOWN, buff=0.3)
            self.play(Write(components))
            self.wait(0.5)
            
            # Response
            response_arrow = Arrow(server.get_left(), user.get_right() + DOWN * 0.5, color=GREEN, buff=0.3)
            response_text = Text("HTML/JSON", font_size=18, color=GREEN).next_to(response_arrow, UP, buff=0.1)
            
            self.play(Create(response_arrow), Write(response_text))
        
        with self.voiceover(text="Here's an example of a JSON response from an API call. The server returns structured data that the application can use. But here's the critical question: what happens when traffic grows? This single server becomes a bottleneck.") as tracker:
            # Show JSON example
            json_example = Code(
                code='''
{
  "id": 12,
  "name": "John",
  "status": "active"
}
                ''',
                language="json",
                font_size=16,
                background="window",
                insert_line_no=False
            ).scale(0.6).shift(DOWN * 2)
            
            self.play(Create(json_example))
            self.wait(2)
            
            # Show warning
            warning = Text("⚠ Single Point of Failure!", font_size=28, color=RED)
            warning.to_edge(DOWN, buff=0.5)
            self.play(Write(warning))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def separating_web_and_database(self):
        with self.voiceover(text="Chapter Two: Separating Web and Database Tiers. As our user base grows, we need to improve our architecture. The first major step is separating the web tier from the data tier.") as tracker:
            chapter_title = Text("Chapter 2: Separating Tiers", font_size=40, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="We start with our single server containing everything. Watch as we split it into two independent components: the web server tier and the database server tier.") as tracker:
            # Single server
            single_server = Rectangle(height=3, width=2.5, color=ORANGE, fill_opacity=0.4)
            server_text = Text("Single Server", font_size=22, color=WHITE).move_to(single_server.get_top() + DOWN * 0.4)
            
            components_text = VGroup(
                Text("• Web App", font_size=18),
                Text("• Database", font_size=18),
                Text("• Cache", font_size=18)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            components_text.move_to(single_server.get_center() + DOWN * 0.3)
            
            single_group = VGroup(single_server, server_text, components_text)
            
            self.play(Create(single_server), Write(server_text), Write(components_text))
            self.wait(1)
        
        with self.voiceover(text="The single server splits into two separate tiers. On the left, we have the web and mobile traffic tier, which handles all user requests. On the right, we have the dedicated data tier for our database.") as tracker:
            # Split animation
            web_server = Rectangle(height=2.5, width=2, color=GREEN, fill_opacity=0.4).shift(LEFT * 3)
            web_text = Text("Web Tier", font_size=24, color=WHITE).move_to(web_server.get_top() + DOWN * 0.4)
            web_label = Text("Handles HTTP\nRequests", font_size=16).move_to(web_server.get_center() + DOWN * 0.3)
            
            db_server = Rectangle(height=2.5, width=2, color=BLUE, fill_opacity=0.4).shift(RIGHT * 3)
            db_text = Text("Data Tier", font_size=24, color=WHITE).move_to(db_server.get_top() + DOWN * 0.4)
            db_label = Text("Stores Data\n& State", font_size=16).move_to(db_server.get_center() + DOWN * 0.3)
            
            # Connection
            connection = Arrow(web_server.get_right(), db_server.get_left(), color=YELLOW, buff=0.1)
            connection_label = Text("SQL Queries", font_size=14, color=YELLOW).next_to(connection, UP, buff=0.1)
            
            self.play(
                Transform(single_group, VGroup(web_server, web_text, web_label)),
                run_time=1.5
            )
            self.play(
                FadeIn(db_server),
                Write(db_text),
                Write(db_label)
            )
            self.play(Create(connection), Write(connection_label))
        
        with self.voiceover(text="This separation brings a huge benefit: independent scaling! We can now scale the web tier and data tier separately based on their individual needs. This is a fundamental principle of scalable architecture.") as tracker:
            benefit = Text("✓ Independent Scaling!", font_size=32, color=GREEN, weight=BOLD)
            benefit.to_edge(UP, buff=0.5)
            self.play(Write(benefit))
            self.wait(1.5)
            
            scale_web = Text("Scale Web Tier ↔", font_size=20, color=GREEN).next_to(web_server, DOWN, buff=0.5)
            scale_db = Text("Scale Data Tier ↕", font_size=20, color=BLUE).next_to(db_server, DOWN, buff=0.5)
            
            self.play(Write(scale_web), Write(scale_db))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now let's talk about database choices. We have two main categories: Relational databases and NoSQL databases. Relational databases like MySQL, PostgreSQL, and Oracle store data in tables with rows and columns. They use SQL for querying and enforce strict schemas.") as tracker:
            title = Text("Database Types", font_size=36, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            # Relational DB
            rdb_title = Text("Relational Databases", font_size=28, color=GREEN).shift(LEFT * 3.5 + UP * 1.5)
            rdb_box = Rectangle(height=2.5, width=3, color=GREEN, fill_opacity=0.2).shift(LEFT * 3.5 + DOWN * 0.5)
            
            # Table visualization
            table = Table(
                [["1", "John"], ["2", "Jane"], ["3", "Bob"]],
                col_labels=[Text("ID"), Text("Name")],
                include_outer_lines=True
            ).scale(0.4).move_to(rdb_box.get_center())
            
            rdb_examples = Text("MySQL • PostgreSQL\nOracle • SQL Server", font_size=14, color=GREEN)
            rdb_examples.next_to(rdb_box, DOWN, buff=0.2)
            
            self.play(Write(rdb_title))
            self.play(Create(rdb_box), Create(table))
            self.play(Write(rdb_examples))
        
        with self.voiceover(text="NoSQL databases include document stores like MongoDB, key-value stores like DynamoDB and Redis, column stores like Cassandra, and graph databases like Neo4j. They offer flexibility, horizontal scalability, and are schema-less.") as tracker:
            # NoSQL DB
            nosql_title = Text("NoSQL Databases", font_size=28, color=ORANGE).shift(RIGHT * 3.5 + UP * 1.5)
            nosql_box = Rectangle(height=2.5, width=3, color=ORANGE, fill_opacity=0.2).shift(RIGHT * 3.5 + DOWN * 0.5)
            
            # Key-value visualization
            kv_data = VGroup(
                Text('{"user": "data"}', font_size=14),
                Text('[1, 2, 3, 4]', font_size=14),
                Text('key → value', font_size=14)
            ).arrange(DOWN, buff=0.2).move_to(nosql_box.get_center())
            
            nosql_examples = Text("MongoDB • Cassandra\nDynamoDB • Redis", font_size=14, color=ORANGE)
            nosql_examples.next_to(nosql_box, DOWN, buff=0.2)
            
            self.play(Write(nosql_title))
            self.play(Create(nosql_box), Create(kv_data))
            self.play(Write(nosql_examples))
            self.wait(1)
        
        with self.voiceover(text="When should you use each type? Relational databases are perfect for applications requiring complex queries, transactions, and strong consistency. Examples include banking systems and e-commerce platforms. NoSQL databases excel at handling massive scale, flexible schemas, and high write throughput. Think social media feeds, real-time analytics, and session storage.") as tracker:
            use_cases_title = Text("When to Use Each?", font_size=30, color=YELLOW)
            use_cases_title.move_to(DOWN * 2.5)
            
            self.play(Write(use_cases_title))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def vertical_vs_horizontal_scaling(self):
        with self.voiceover(text="Chapter Three: Vertical versus Horizontal Scaling. Now that we've separated our tiers, we need to understand how to scale them. There are two fundamental approaches: vertical scaling and horizontal scaling.") as tracker:
            chapter_title = Text("Chapter 3: Scaling Strategies", font_size=40, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="Vertical scaling, also called scaling up, means adding more power to your existing server. You increase the CPU, add more RAM, or upgrade to faster storage. It's like replacing your car's engine with a bigger, more powerful one.") as tracker:
            # Left side - Vertical Scaling
            vertical_title = Text("Vertical Scaling", font_size=30, color=ORANGE).shift(LEFT * 3.5 + UP * 2.5)
            vertical_subtitle = Text("(Scale Up)", font_size=20, color=ORANGE).next_to(vertical_title, DOWN, buff=0.2)
            
            self.play(Write(vertical_title), Write(vertical_subtitle))
            
            # Server growing animation
            server_base = Rectangle(height=1.5, width=1.2, color=ORANGE, fill_opacity=0.3).shift(LEFT * 3.5 + UP * 0.3)
            
            cpu_label = Text("CPU", font_size=16).move_to(server_base.get_center() + UP * 0.5)
            ram_label = Text("RAM", font_size=16).move_to(server_base.get_center())
            disk_label = Text("Disk", font_size=16).move_to(server_base.get_center() + DOWN * 0.5)
            
            # Resource bars
            cpu_bar = Rectangle(height=0.2, width=0.8, color=RED, fill_opacity=0.7).next_to(cpu_label, RIGHT, buff=0.2)
            ram_bar = Rectangle(height=0.2, width=0.8, color=BLUE, fill_opacity=0.7).next_to(ram_label, RIGHT, buff=0.2)
            disk_bar = Rectangle(height=0.2, width=0.8, color=GREEN, fill_opacity=0.7).next_to(disk_label, RIGHT, buff=0.2)
            
            self.play(Create(server_base))
            self.play(Write(cpu_label), Write(ram_label), Write(disk_label))
            self.play(Create(cpu_bar), Create(ram_bar), Create(disk_bar))
            
            # Growing animation
            cpu_bar_grown = Rectangle(height=0.2, width=1.8, color=RED, fill_opacity=0.9).next_to(cpu_label, RIGHT, buff=0.2)
            ram_bar_grown = Rectangle(height=0.2, width=1.8, color=BLUE, fill_opacity=0.9).next_to(ram_label, RIGHT, buff=0.2)
            disk_bar_grown = Rectangle(height=0.2, width=1.8, color=GREEN, fill_opacity=0.9).next_to(disk_label, RIGHT, buff=0.2)
            
            self.play(
                Transform(cpu_bar, cpu_bar_grown),
                Transform(ram_bar, ram_bar_grown),
                Transform(disk_bar, disk_bar_grown),
                run_time=2
            )
            
            specs_before = Text("4 CPU, 16GB RAM", font_size=14, color=GRAY).shift(LEFT * 3.5 + DOWN * 1)
            specs_after = Text("16 CPU, 128GB RAM", font_size=14, color=GREEN).next_to(specs_before, DOWN, buff=0.2)
            
            self.play(Write(specs_before))
            self.wait(0.5)
            self.play(Write(specs_after))
        
        with self.voiceover(text="Horizontal scaling, or scaling out, means adding more servers to your resource pool. Instead of making one server more powerful, you distribute the load across multiple servers. It's like having a fleet of regular cars instead of one supercar.") as tracker:
            # Right side - Horizontal Scaling
            horizontal_title = Text("Horizontal Scaling", font_size=30, color=GREEN).shift(RIGHT * 3.5 + UP * 2.5)
            horizontal_subtitle = Text("(Scale Out)", font_size=20, color=GREEN).next_to(horizontal_title, DOWN, buff=0.2)
            
            self.play(Write(horizontal_title), Write(horizontal_subtitle))
            
            # Multiple servers appearing
            server1 = Rectangle(height=1, width=0.8, color=GREEN, fill_opacity=0.4).shift(RIGHT * 2.5 + UP * 0.5)
            server1_label = Text("Server 1", font_size=14).move_to(server1.get_center())
            
            self.play(Create(server1), Write(server1_label))
            self.wait(0.3)
            
            server2 = Rectangle(height=1, width=0.8, color=GREEN, fill_opacity=0.4).shift(RIGHT * 3.5 + UP * 0.5)
            server2_label = Text("Server 2", font_size=14).move_to(server2.get_center())
            
            self.play(Create(server2), Write(server2_label))
            self.wait(0.3)
            
            server3 = Rectangle(height=1, width=0.8, color=GREEN, fill_opacity=0.4).shift(RIGHT * 4.5 + UP * 0.5)
            server3_label = Text("Server 3", font_size=14).move_to(server3.get_center())
            
            self.play(Create(server3), Write(server3_label))
            self.wait(0.3)
            
            server4 = Rectangle(height=1, width=0.8, color=GREEN, fill_opacity=0.4).shift(RIGHT * 2.5 + DOWN * 0.8)
            server4_label = Text("Server 4", font_size=14).move_to(server4.get_center())
            
            server5 = Rectangle(height=1, width=0.8, color=GREEN, fill_opacity=0.4).shift(RIGHT * 3.5 + DOWN * 0.8)
            server5_label = Text("Server 5", font_size=14).move_to(server5.get_center())
            
            server6 = Rectangle(height=1, width=0.8, color=GREEN, fill_opacity=0.4).shift(RIGHT * 4.5 + DOWN * 0.8)
            server6_label = Text("Server 6", font_size=14).move_to(server6.get_center())
            
            self.play(
                Create(server4), Write(server4_label),
                Create(server5), Write(server5_label),
                Create(server6), Write(server6_label)
            )
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Vertical scaling has serious limitations. First, there's a hard limit to how much you can upgrade a single server. You can't add unlimited CPU or RAM. Second, and more critically, it creates a single point of failure. If that one powerful server goes down, your entire system goes offline.") as tracker:
            limitations_title = Text("Vertical Scaling Limitations", font_size=32, color=RED)
            limitations_title.to_edge(UP, buff=0.5)
            self.play(Write(limitations_title))
            
            # Limitation 1: Hard limit
            limit1_icon = Text("⚠", font_size=60, color=RED).shift(LEFT * 4 + UP * 0.5)
            limit1_title = Text("Hard Limit", font_size=26, color=ORANGE).next_to(limit1_icon, RIGHT, buff=0.5)
            limit1_desc = Text("Can't infinitely upgrade\na single machine", font_size=18, color=GRAY)
            limit1_desc.next_to(limit1_title, DOWN, buff=0.3, aligned_edge=LEFT)
            
            # Ceiling visualization
            ceiling = Line(LEFT * 2 + UP * 1, RIGHT * 0 + UP * 1, color=RED, stroke_width=8)
            arrow_up = Arrow(LEFT * 1 + DOWN * 0.5, LEFT * 1 + UP * 0.8, color=ORANGE, buff=0.1)
            blocked = Text("✗", font_size=40, color=RED).next_to(arrow_up, UP, buff=0.1)
            
            ceiling_group = VGroup(ceiling, arrow_up, blocked).shift(LEFT * 3.5)
            
            self.play(Write(limit1_icon), Write(limit1_title))
            self.play(Write(limit1_desc))
            self.play(Create(ceiling_group))
            self.wait(1)
            
            # Limitation 2: Single Point of Failure
            limit2_icon = Text("💥", font_size=60, color=RED).shift(RIGHT * 1.5 + UP * 0.5)
            limit2_title = Text("Single Point of Failure", font_size=26, color=ORANGE).next_to(limit2_icon, RIGHT, buff=0.5)
            limit2_desc = Text("One server fails =\nEntire system down", font_size=18, color=GRAY)
            limit2_desc.next_to(limit2_title, DOWN, buff=0.3, aligned_edge=LEFT)
            
            # SPOF visualization
            single_server = Rectangle(height=1.2, width=1, color=ORANGE, fill_opacity=0.5).shift(RIGHT * 2 + DOWN * 1.2)
            x_mark = Text("✗", font_size=80, color=RED).move_to(single_server.get_center())
            
            system_text = Text("SYSTEM DOWN", font_size=20, color=RED, weight=BOLD)
            system_text.next_to(single_server, DOWN, buff=0.3)
            
            self.play(Write(limit2_icon), Write(limit2_title))
            self.play(Write(limit2_desc))
            self.play(Create(single_server))
            self.wait(0.5)
            self.play(Write(x_mark), Write(system_text))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Horizontal scaling is the clear winner for large-scale systems. It offers virtually unlimited scaling potential, built-in redundancy, and better fault tolerance. If one server fails, others continue serving traffic. This is why tech giants like Google, Facebook, and Amazon all use horizontal scaling.") as tracker:
            advantages_title = Text("Horizontal Scaling Advantages", font_size=32, color=GREEN)
            advantages_title.to_edge(UP, buff=0.5)
            self.play(Write(advantages_title))
            
            # Advantage 1
            adv1 = Text("✓ Unlimited Scaling Potential", font_size=26, color=GREEN).shift(UP * 1.5)
            adv1_desc = Text("Add as many servers as needed", font_size=18, color=GRAY).next_to(adv1, DOWN, buff=0.2)
            
            self.play(Write(adv1))
            self.play(Write(adv1_desc))
            self.wait(1)
            
            # Advantage 2
            adv2 = Text("✓ Built-in Redundancy", font_size=26, color=GREEN).shift(UP * 0.1)
            adv2_desc = Text("Multiple servers ensure reliability", font_size=18, color=GRAY).next_to(adv2, DOWN, buff=0.2)
            
            self.play(Write(adv2))
            self.play(Write(adv2_desc))
            self.wait(1)
            
            # Advantage 3
            adv3 = Text("✓ Fault Tolerance", font_size=26, color=GREEN).shift(DOWN * 1.3)
            adv3_desc = Text("System stays up even if servers fail", font_size=18, color=GRAY).next_to(adv3, DOWN, buff=0.2)
            
            self.play(Write(adv3))
            self.play(Write(adv3_desc))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def load_balancer(self):
        with self.voiceover(text="Chapter Four: Load Balancer. To effectively distribute traffic across multiple servers, we need a load balancer. The load balancer is the traffic cop of our system, intelligently routing requests to available servers.") as tracker:
            chapter_title = Text("Chapter 4: Load Balancer", font_size=40, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="Here's the architecture with a load balancer. Users no longer connect directly to web servers. Instead, they connect to the load balancer's public IP address. The load balancer then distributes requests to web servers with private IPs for enhanced security.") as tracker:
            # Users
            user1 = self.create_user_icon().shift(LEFT * 6 + UP * 2)
            user2 = self.create_user_icon().shift(LEFT * 6)
            user3 = self.create_user_icon().shift(LEFT * 6 + DOWN * 2)
            
            user1_label = Text("User 1", font_size=14).next_to(user1, LEFT, buff=0.2)
            user2_label = Text("User 2", font_size=14).next_to(user2, LEFT, buff=0.2)
            user3_label = Text("User 3", font_size=14).next_to(user3, LEFT, buff=0.2)
            
            self.play(
                FadeIn(user1), FadeIn(user2), FadeIn(user3),
                Write(user1_label), Write(user2_label), Write(user3_label)
            )
            
            # Load Balancer
            lb_box = Rectangle(height=2.5, width=2, color=PURPLE, fill_opacity=0.5).shift(LEFT * 2)
            lb_text = Text("Load\nBalancer", font_size=24, color=WHITE, weight=BOLD).move_to(lb_box.get_center())
            lb_ip = Text("Public IP:\n203.0.113.5", font_size=14, color=YELLOW).next_to(lb_box, DOWN, buff=0.2)
            
            self.play(Create(lb_box), Write(lb_text))
            self.play(Write(lb_ip))
            
            # Web Servers
            server1 = Rectangle(height=1.5, width=1.5, color=GREEN, fill_opacity=0.4).shift(RIGHT * 2.5 + UP * 1.5)
            server1_text = Text("Server 1", font_size=18).move_to(server1.get_center())
            server1_ip = Text("Private IP:\n10.0.1.1", font_size=12, color=GRAY).next_to(server1, DOWN, buff=0.2)
            
            server2 = Rectangle(height=1.5, width=1.5, color=GREEN, fill_opacity=0.4).shift(RIGHT * 2.5 + DOWN * 1.5)
            server2_text = Text("Server 2", font_size=18).move_to(server2.get_center())
            server2_ip = Text("Private IP:\n10.0.1.2", font_size=12, color=GRAY).next_to(server2, DOWN, buff=0.2)
            
            self.play(
                Create(server1), Write(server1_text), Write(server1_ip),
                Create(server2), Write(server2_text), Write(server2_ip)
            )
        
        with self.voiceover(text="Watch how traffic flows through the system. The load balancer receives requests from all users and intelligently distributes them to healthy servers. This ensures no single server gets overwhelmed.") as tracker:
            # Traffic flow
            arrow1 = Arrow(user1.get_right(), lb_box.get_left() + UP * 0.5, color=YELLOW, buff=0.1, stroke_width=3)
            arrow2 = Arrow(user2.get_right(), lb_box.get_left(), color=YELLOW, buff=0.1, stroke_width=3)
            arrow3 = Arrow(user3.get_right(), lb_box.get_left() + DOWN * 0.5, color=YELLOW, buff=0.1, stroke_width=3)
            
            self.play(Create(arrow1), Create(arrow2), Create(arrow3))
            self.wait(0.5)
            
            # Distribution to servers
            dist1 = Arrow(lb_box.get_right() + UP * 0.3, server1.get_left(), color=GREEN, buff=0.1, stroke_width=3)
            dist2 = Arrow(lb_box.get_right() + DOWN * 0.3, server2.get_left(), color=GREEN, buff=0.1, stroke_width=3)
            
            self.play(Create(dist1), Create(dist2))
            
            # Load indicators
            load1 = Text("50% Load", font_size=16, color=GREEN).next_to(server1, RIGHT, buff=0.3)
            load2 = Text("50% Load", font_size=16, color=GREEN).next_to(server2, RIGHT, buff=0.3)
            
            self.play(Write(load1), Write(load2))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now let's see the magic of failover. Imagine Server 1 crashes or becomes unresponsive. The load balancer detects this failure immediately through health checks.") as tracker:
            # Recreate scene
            lb_box = Rectangle(height=2.5, width=2, color=PURPLE, fill_opacity=0.5).shift(LEFT * 2)
            lb_text = Text("Load\nBalancer", font_size=24, color=WHITE, weight=BOLD).move_to(lb_box.get_center())
            
            server1 = Rectangle(height=1.5, width=1.5, color=GREEN, fill_opacity=0.4).shift(RIGHT * 2.5 + UP * 1.5)
            server1_text = Text("Server 1", font_size=18, color=WHITE).move_to(server1.get_center())
            
            server2 = Rectangle(height=1.5, width=1.5, color=GREEN, fill_opacity=0.4).shift(RIGHT * 2.5 + DOWN * 1.5)
            server2_text = Text("Server 2", font_size=18, color=WHITE).move_to(server2.get_center())
            
            self.play(
                Create(lb_box), Write(lb_text),
                Create(server1), Write(server1_text),
                Create(server2), Write(server2_text)
            )
            
            # Server 1 fails
            server1_failed = Rectangle(height=1.5, width=1.5, color=RED, fill_opacity=0.6).shift(RIGHT * 2.5 + UP * 1.5)
            x_mark = Text("✗", font_size=60, color=RED).move_to(server1_failed.get_center())
            offline_label = Text("OFFLINE", font_size=16, color=RED, weight=BOLD).next_to(server1_failed, UP, buff=0.2)
            
            self.play(
                Transform(server1, server1_failed),
                Write(x_mark),
                Write(offline_label)
            )
            self.wait(1)
        
        with self.voiceover(text="All traffic is automatically rerouted to Server 2. The system remains online and responsive. Users experience no downtime. This is the power of redundancy!") as tracker:
            # All traffic to server 2
            users = VGroup(
                self.create_user_icon().shift(LEFT * 5 + UP * 1.5),
                self.create_user_icon().shift(LEFT * 5),
                self.create_user_icon().shift(LEFT * 5 + DOWN * 1.5)
            )
            
            self.play(FadeIn(users))
            
            traffic_arrows = VGroup(
                Arrow(users[0].get_right(), lb_box.get_left() + UP * 0.5, color=YELLOW, buff=0.1),
                Arrow(users[1].get_right(), lb_box.get_left(), color=YELLOW, buff=0.1),
                Arrow(users[2].get_right(), lb_box.get_left() + DOWN * 0.5, color=YELLOW, buff=0.1)
            )
            
            redirect_arrow = Arrow(lb_box.get_right() + DOWN * 0.3, server2.get_left(), color=GREEN, buff=0.1, stroke_width=6)
            
            self.play(Create(traffic_arrows))
            self.play(Create(redirect_arrow))
            
            load_label = Text("100% Load", font_size=18, color=ORANGE, weight=BOLD).next_to(server2, RIGHT, buff=0.3)
            self.play(Write(load_label))
            self.wait(1)
        
        with self.voiceover(text="Once a new healthy server is added to the pool, the load balancer automatically includes it in the rotation. Traffic is distributed evenly again, and the system returns to optimal performance.") as tracker:
            # Add new server
            server3 = Rectangle(height=1.5, width=1.5, color=GREEN, fill_opacity=0.4).shift(RIGHT * 5.5)
            server3_text = Text("Server 3", font_size=18, color=WHITE).move_to(server3.get_center())
            healthy_label = Text("✓ HEALTHY", font_size=16, color=GREEN, weight=BOLD).next_to(server3, UP, buff=0.2)
            
            self.play(
                Create(server3),
                Write(server3_text),
                Write(healthy_label)
            )
            
            new_arrow = Arrow(lb_box.get_right(), server3.get_left(), color=GREEN, buff=0.1, stroke_width=3)
            self.play(Create(new_arrow))
            
            # Update loads
            load2_new = Text("50% Load", font_size=16, color=GREEN).move_to(load_label.get_center())
            load3 = Text("50% Load", font_size=16, color=GREEN).next_to(server3, RIGHT, buff=0.3)
            
            self.play(Transform(load_label, load2_new), Write(load3))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def database_replication(self):
        with self.voiceover(text="Chapter Five: Database Replication. Now let's tackle the data tier. With a load balancer handling the web tier, we have high availability for our web servers. But what about our database? We need database replication.") as tracker:
            chapter_title = Text("Chapter 5: Database Replication", font_size=40, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="The most common replication setup is master-slave replication. The master database handles all write operations: inserts, updates, and deletes. Slave databases get copies of the data from the master and handle read operations.") as tracker:
            # Master DB
            master_db = self.create_database_icon(color=BLUE).shift(UP * 1.5)
            master_label = Text("Master DB", font_size=24, color=BLUE, weight=BOLD).next_to(master_db, UP, buff=0.3)
            master_role = Text("Handles WRITES", font_size=16, color=ORANGE).next_to(master_db, DOWN, buff=0.3)
            
            self.play(FadeIn(master_db), Write(master_label), Write(master_role))
            self.wait(0.5)
            
            # Slave DBs
            slave1 = self.create_database_icon(color=GREEN).shift(LEFT * 3 + DOWN * 1.5)
            slave1_label = Text("Slave 1", font_size=20, color=GREEN).next_to(slave1, DOWN, buff=0.2)
            
            slave2 = self.create_database_icon(color=GREEN).shift(RIGHT * 0 + DOWN * 1.5)
            slave2_label = Text("Slave 2", font_size=20, color=GREEN).next_to(slave2, DOWN, buff=0.2)
            
            slave3 = self.create_database_icon(color=GREEN).shift(RIGHT * 3 + DOWN * 1.5)
            slave3_label = Text("Slave 3", font_size=20, color=GREEN).next_to(slave3, DOWN, buff=0.2)
            
            self.play(
                FadeIn(slave1), Write(slave1_label),
                FadeIn(slave2), Write(slave2_label),
                FadeIn(slave3), Write(slave3_label)
            )
            
            read_label = Text("Handle READS", font_size=16, color=GREEN).next_to(slave2, DOWN, buff=1)
            self.play(Write(read_label))
        
        with self.voiceover(text="Watch how data flows in this architecture. Write operations go to the master database. The master then replicates this data to all slave databases. This happens continuously to keep the slaves synchronized with the master.") as tracker:
            # Write operation
            write_op = Text("INSERT user", font_size=18, color=ORANGE, weight=BOLD).shift(LEFT * 6 + UP * 1.5)
            write_arrow = Arrow(write_op.get_right(), master_db.get_left(), color=ORANGE, buff=0.2, stroke_width=4)
            
            self.play(Write(write_op))
            self.play(Create(write_arrow))
            self.wait(0.5)
            
            # Replication
            repl1 = Arrow(master_db.get_bottom() + LEFT * 0.3, slave1.get_top(), color=BLUE, buff=0.1, stroke_width=3)
            repl2 = Arrow(master_db.get_bottom(), slave2.get_top(), color=BLUE, buff=0.1, stroke_width=3)
            repl3 = Arrow(master_db.get_bottom() + RIGHT * 0.3, slave3.get_top(), color=BLUE, buff=0.1, stroke_width=3)
            
            repl_label = Text("Data Replication", font_size=16, color=BLUE).shift(UP * 0.2)
            
            self.play(Write(repl_label))
            self.play(Create(repl1), Create(repl2), Create(repl3))
            self.wait(1)
            
            # Read operation
            read_op = Text("SELECT *", font_size=18, color=GREEN, weight=BOLD).shift(RIGHT * 6 + DOWN * 1.5)
            read_arrow = Arrow(read_op.get_left(), slave3.get_right(), color=GREEN, buff=0.2, stroke_width=4)
            
            self.play(Write(read_op))
            self.play(Create(read_arrow))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Database replication provides three major benefits. First, better performance: most applications have far more read operations than writes. By distributing reads across multiple slaves, we can handle much more traffic.") as tracker:
            benefits_title = Text("Benefits of Replication", font_size=36, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(benefits_title))
            
            # Benefit 1: Performance
            perf_icon = Text("⚡", font_size=60, color=YELLOW).shift(LEFT * 4 + UP * 0.8)
            perf_title = Text("Better Performance", font_size=28, color=GREEN).next_to(perf_icon, RIGHT, buff=0.5)
            perf_desc = VGroup(
                Text("• Parallel read queries", font_size=18),
                Text("• Distribute load", font_size=18),
                Text("• Handle more traffic", font_size=18)
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(perf_title, DOWN, buff=0.3, aligned_edge=LEFT)
            
            self.play(Write(perf_icon), Write(perf_title))
            self.play(Write(perf_desc))
            self.wait(2)
        
        with self.voiceover(text="Second, reliability. Data is stored across multiple servers. If one database disk fails, data is not lost because it exists on other databases. This redundancy is critical for data safety.") as tracker:
            # Benefit 2: Reliability
            self.play(FadeOut(perf_icon), FadeOut(perf_title), FadeOut(perf_desc))
            
            rel_icon = Text("🛡", font_size=60, color=BLUE).shift(LEFT * 4 + UP * 0.8)
            rel_title = Text("Reliability", font_size=28, color=GREEN).next_to(rel_icon, RIGHT, buff=0.5)
            rel_desc = VGroup(
                Text("• Data redundancy", font_size=18),
                Text("• Protection from disk failures", font_size=18),
                Text("• Multiple data copies", font_size=18)
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(rel_title, DOWN, buff=0.3, aligned_edge=LEFT)
            
            self.play(Write(rel_icon), Write(rel_title))
            self.play(Write(rel_desc))
            self.wait(2)
        
        with self.voiceover(text="Third, high availability. Even if the master database goes offline temporarily, your system can continue serving read requests from slave databases. We can also promote a slave to become the new master.") as tracker:
            # Benefit 3: High Availability
            self.play(FadeOut(rel_icon), FadeOut(rel_title), FadeOut(rel_desc))
            
            ha_icon = Text("✓✓✓", font_size=60, color=GREEN).shift(LEFT * 4 + UP * 0.8)
            ha_title = Text("High Availability", font_size=28, color=GREEN).next_to(ha_icon, RIGHT, buff=0.5)
            ha_desc = VGroup(
                Text("• System stays online", font_size=18),
                Text("• Continue serving reads", font_size=18),
                Text("• Automatic failover", font_size=18)
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(ha_title, DOWN, buff=0.3, aligned_edge=LEFT)
            
            self.play(Write(ha_icon), Write(ha_title))
            self.play(Write(ha_desc))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let's examine the failure scenarios. If a slave database goes offline, read operations are temporarily redirected to the master or other slave databases. A new slave can be created to replace the failed one.") as tracker:
            scenario_title = Text("Failure Scenarios", font_size=36, color=RED).to_edge(UP, buff=0.5)
            self.play(Write(scenario_title))
            
            # Slave failure scenario
            master = self.create_database_icon(color=BLUE).shift(UP * 1)
            master_label = Text("Master", font_size=18).next_to(master, UP, buff=0.2)
            
            slave_healthy = self.create_database_icon(color=GREEN).shift(LEFT * 2.5 + DOWN * 1.5)
            slave_healthy_label = Text("Slave 1\n✓ Healthy", font_size=16, color=GREEN).next_to(slave_healthy, DOWN, buff=0.2)
            
            slave_failed = self.create_database_icon(color=RED).shift(RIGHT * 2.5 + DOWN * 1.5)
            slave_failed_label = Text("Slave 2\n✗ Offline", font_size=16, color=RED).next_to(slave_failed, DOWN, buff=0.2)
            
            self.play(
                FadeIn(master), Write(master_label),
                FadeIn(slave_healthy), Write(slave_healthy_label),
                FadeIn(slave_failed), Write(slave_failed_label)
            )
            
            redirect = Text("Reads → Master or Slave 1", font_size=20, color=ORANGE, weight=BOLD)
            redirect.shift(DOWN * 3)
            self.play(Write(redirect))
            self.wait(2)
        
        with self.voiceover(text="If the master database fails, things are more complex. A slave database is promoted to be the new master. In production, this promotion can be automatic or manual depending on your setup. A new slave is then added to replace the promoted one. This ensures continuous operation.") as tracker:
            self.play(FadeOut(*self.mobjects))
            
            scenario_title2 = Text("Master Failure Scenario", font_size=36, color=RED).to_edge(UP, buff=0.5)
            self.play(Write(scenario_title2))
            
            # Master fails
            master_failed = self.create_database_icon(color=RED).shift(UP * 1.5)
            master_failed_label = Text("Master\n✗ Offline", font_size=18, color=RED).next_to(master_failed, UP, buff=0.2)
            
            slave1_before = self.create_database_icon(color=GREEN).shift(LEFT * 3 + DOWN * 1)
            slave1_label = Text("Slave 1", font_size=16).next_to(slave1_before, DOWN, buff=0.2)
            
            slave2_before = self.create_database_icon(color=GREEN).shift(RIGHT * 3 + DOWN * 1)
            slave2_label = Text("Slave 2", font_size=16).next_to(slave2_before, DOWN, buff=0.2)
            
            self.play(
                FadeIn(master_failed), Write(master_failed_label),
                FadeIn(slave1_before), Write(slave1_label),
                FadeIn(slave2_before), Write(slave2_label)
            )
            self.wait(1)
            
            # Promotion
            promote_arrow = Arrow(slave1_before.get_top(), master_failed.get_left(), color=YELLOW, buff=0.2, stroke_width=5)
            promote_text = Text("PROMOTE", font_size=20, color=YELLOW, weight=BOLD).next_to(promote_arrow, LEFT, buff=0.2)
            
            self.play(Create(promote_arrow), Write(promote_text))
            self.wait(0.5)
            
            new_master = self.create_database_icon(color=BLUE).shift(UP * 1.5)
            new_master_label = Text("New Master\n(was Slave 1)", font_size=16, color=BLUE).next_to(new_master, UP, buff=0.2)
            
            self.play(
                FadeOut(master_failed), FadeOut(master_failed_label),
                FadeOut(slave1_before), FadeOut(slave1_label),
                FadeOut(promote_arrow), FadeOut(promote_text),
                FadeIn(new_master), Write(new_master_label)
            )
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def cache_layer(self):
        with self.voiceover(text="Chapter Six: Cache Layer. After scaling the database, we need to address another performance bottleneck. Repeatedly querying the database for the same data is expensive. This is where caching comes in. A cache is a temporary storage layer that stores frequently accessed data in memory.") as tracker:
            chapter_title = Text("Chapter 6: Cache Layer", font_size=40, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="Here's how the cache tier fits into our architecture. It sits between the web application and the database. When a web server needs data, it checks the cache first. This is much faster than querying the database.") as tracker:
            # Web Server
            web_server = Rectangle(height=1.5, width=2, color=GREEN, fill_opacity=0.4).shift(LEFT * 4 + UP * 1.5)
            web_text = Text("Web Server", font_size=20).move_to(web_server.get_center())
            
            # Cache
            cache = Rectangle(height=1.5, width=2, color=ORANGE, fill_opacity=0.4).shift(UP * 1.5)
            cache_text = Text("Cache", font_size=20).move_to(cache.get_center())
            cache_subtitle = Text("(Memcached/Redis)", font_size=14, color=GRAY).next_to(cache, DOWN, buff=0.2)
            
            # Database
            database = self.create_database_icon(color=BLUE).shift(RIGHT * 4 + UP * 1.5)
            db_label = Text("Database", font_size=20).next_to(database, DOWN, buff=0.3)
            
            self.play(
                Create(web_server), Write(web_text),
                Create(cache), Write(cache_text), Write(cache_subtitle),
                FadeIn(database), Write(db_label)
            )
            
            # Connections
            web_to_cache = Arrow(web_server.get_right(), cache.get_left(), color=YELLOW, buff=0.1)
            cache_to_db = Arrow(cache.get_right(), database.get_left(), color=BLUE, buff=0.1)
            
            self.play(Create(web_to_cache), Create(cache_to_db))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let me walk you through the cache workflow step by step. Step one: The web server receives a request and checks the cache for the required data. Step two: If the data exists in the cache, we call this a cache hit. The data is returned immediately. This is the fast path.") as tracker:
            workflow_title = Text("Cache Workflow", font_size=36, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(workflow_title))
            
            # Setup
            web = Rectangle(height=1.2, width=1.8, color=GREEN, fill_opacity=0.4).shift(LEFT * 4)
            web_label = Text("Web", font_size=18).move_to(web.get_center())
            
            cache_box = Rectangle(height=1.2, width=1.8, color=ORANGE, fill_opacity=0.4)
            cache_label = Text("Cache", font_size=18).move_to(cache_box.get_center())
            
            db_box = Rectangle(height=1.2, width=1.8, color=BLUE, fill_opacity=0.4).shift(RIGHT * 4)
            db_label = Text("DB", font_size=18).move_to(db_box.get_center())
            
            self.play(
                Create(web), Write(web_label),
                Create(cache_box), Write(cache_label),
                Create(db_box), Write(db_label)
            )
            
            # Step 1: Check cache
            step1 = Text("1. Check Cache", font_size=24, color=YELLOW).shift(DOWN * 1.5)
            check_arrow = Arrow(web.get_right(), cache_box.get_left(), color=YELLOW, buff=0.1, stroke_width=4)
            
            self.play(Write(step1))
            self.play(Create(check_arrow))
            self.wait(1)
            
            # Step 2: Cache Hit
            self.play(FadeOut(step1))
            step2 = Text("2. Cache HIT - Return Data", font_size=24, color=GREEN).shift(DOWN * 1.5)
            hit_label = Text("✓ FOUND", font_size=20, color=GREEN, weight=BOLD).next_to(cache_box, UP, buff=0.3)
            return_arrow = Arrow(cache_box.get_left(), web.get_right(), color=GREEN, buff=0.1, stroke_width=4)
            speed_text = Text("⚡ Fast!", font_size=18, color=GREEN).next_to(return_arrow, DOWN, buff=0.1)
            
            self.play(Write(step2), Write(hit_label))
            self.play(Create(return_arrow), Write(speed_text))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Step three: If the data is not in the cache, we have a cache miss. The web server must query the database to retrieve the data. This is slower but necessary. Step four: The retrieved data is stored in the cache for future requests. Step five: The data is returned to the web server. Next time this data is requested, it will be a cache hit.") as tracker:
            workflow_title = Text("Cache Workflow (continued)", font_size=36, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(workflow_title))
            
            # Setup
            web = Rectangle(height=1.2, width=1.8, color=GREEN, fill_opacity=0.4).shift(LEFT * 4.5)
            web_label = Text("Web", font_size=18).move_to(web.get_center())
            
            cache_box = Rectangle(height=1.2, width=1.8, color=ORANGE, fill_opacity=0.4).shift(LEFT * 0.5)
            cache_label = Text("Cache", font_size=18).move_to(cache_box.get_center())
            
            db_box = Rectangle(height=1.2, width=1.8, color=BLUE, fill_opacity=0.4).shift(RIGHT * 3.5)
            db_label = Text("DB", font_size=18).move_to(db_box.get_center())
            
            self.play(
                Create(web), Write(web_label),
                Create(cache_box), Write(cache_label),
                Create(db_box), Write(db_label)
            )
            
            # Step 3: Cache Miss
            step3 = Text("3. Cache MISS", font_size=24, color=RED).shift(UP * 2.2)
            miss_label = Text("✗ NOT FOUND", font_size=18, color=RED, weight=BOLD).next_to(cache_box, UP, buff=0.2)
            
            self.play(Write(step3), Write(miss_label))
            self.wait(0.5)
            
            # Query DB
            query_arrow = Arrow(cache_box.get_right(), db_box.get_left(), color=RED, buff=0.1, stroke_width=4)
            query_text = Text("Query", font_size=16, color=RED).next_to(query_arrow, UP, buff=0.1)
            
            self.play(Create(query_arrow), Write(query_text))
            self.wait(1)
            
            # Step 4: Store in cache
            self.play(FadeOut(step3))
            step4 = Text("4. Store in Cache", font_size=24, color=ORANGE).shift(UP * 2.2)
            db_return = Arrow(db_box.get_left(), cache_box.get_right(), color=BLUE, buff=0.1, stroke_width=4)
            store_text = Text("Store", font_size=16, color=BLUE).next_to(db_return, DOWN, buff=0.1)
            
            self.play(Write(step4))
            self.play(Create(db_return), Write(store_text))
            self.wait(1)
            
            # Step 5: Return to web
            self.play(FadeOut(step4))
            step5 = Text("5. Return Data", font_size=24, color=GREEN).shift(UP * 2.2)
            final_return = Arrow(cache_box.get_left(), web.get_right(), color=GREEN, buff=0.1, stroke_width=4)
            
            self.play(Write(step5))
            self.play(Create(final_return))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Here's a quick example using Memcached code. We try to get data from the cache using the get function. If it's not there, we query the database, then set the data in the cache for next time. Simple but powerful!") as tracker:
            code_title = Text("Memcached Example", font_size=32, color=ORANGE).to_edge(UP, buff=0.5)
            self.play(Write(code_title))
            
            code = Code(
                code='''
# Try to get from cache
data = cache.get("user:123")

if data is None:
    # Cache miss - query database
    data = db.query("SELECT * FROM users WHERE id=123")
    
    # Store in cache for next time
    cache.set("user:123", data, expiration=3600)

return data
                ''',
                language="python",
                font_size=16,
                background="window",
                insert_line_no=False
            ).scale(0.7)
            
            self.play(Create(code))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="When implementing cache, there are several important considerations. First, expiration policy: decide when to expire cached data. Too short and you lose benefits, too long and data becomes stale. Second, consistency: keeping cache and database in sync is challenging, especially during updates.") as tracker:
            considerations_title = Text("Cache Considerations", font_size=36, color=ORANGE).to_edge(UP, buff=0.5)
            self.play(Write(considerations_title))
            
            # Consideration 1: Expiration
            exp_icon = Text("🕐", font_size=50).shift(LEFT * 3 + UP * 0.8)
            exp_title = Text("Expiration Policy", font_size=24, color=YELLOW).next_to(exp_icon, RIGHT, buff=0.4)
            exp_desc = Text("How long to keep data?", font_size=16, color=GRAY).next_to(exp_title, DOWN, buff=0.2, aligned_edge=LEFT)
            exp_example = Text("TTL: 1 hour, 1 day, 1 week?", font_size=14, color=GRAY).next_to(exp_desc, DOWN, buff=0.2, aligned_edge=LEFT)
            
            self.play(Write(exp_icon), Write(exp_title))
            self.play(Write(exp_desc), Write(exp_example))
            self.wait(2)
            
            # Consideration 2: Consistency
            self.play(FadeOut(exp_icon), FadeOut(exp_title), FadeOut(exp_desc), FadeOut(exp_example))
            
            cons_icon = Text("🔄", font_size=50).shift(LEFT * 3 + UP * 0.8)
            cons_title = Text("Consistency", font_size=24, color=BLUE).next_to(cons_icon, RIGHT, buff=0.4)
            cons_desc = Text("Keep cache and DB in sync", font_size=16, color=GRAY).next_to(cons_title, DOWN, buff=0.2, aligned_edge=LEFT)
            cons_challenge = Text("Challenge during updates!", font_size=14, color=RED).next_to(cons_desc, DOWN, buff=0.2, aligned_edge=LEFT)
            
            self.play(Write(cons_icon), Write(cons_title))
            self.play(Write(cons_desc), Write(cons_challenge))
            self.wait(2)
        
        with self.voiceover(text="Third, avoid single point of failure: use multiple cache servers across different data centers for redundancy. Fourth, eviction policies: when the cache is full, which data should be removed? Common strategies are LRU - least recently used, LFU - least frequently used, and FIFO - first in first out.") as tracker:
            self.play(FadeOut(*self.mobjects))
            
            considerations_title = Text("More Considerations", font_size=36, color=ORANGE).to_edge(UP, buff=0.5)
            self.play(Write(considerations_title))
            
            # SPOF
            spof_icon = Text("⚠", font_size=50, color=RED).shift(LEFT * 3 + UP * 0.5)
            spof_title = Text("Avoid Single Point of Failure", font_size=22, color=RED).next_to(spof_icon, RIGHT, buff=0.4)
            spof_solution = Text("Use multiple cache servers", font_size=16, color=GREEN).next_to(spof_title, DOWN, buff=0.2, aligned_edge=LEFT)
            
            self.play(Write(spof_icon), Write(spof_title))
            self.play(Write(spof_solution))
            self.wait(1.5)
            
            # Eviction policies
            evict_title = Text("Eviction Policies", font_size=26, color=PURPLE).shift(DOWN * 0.8)
            
            lru = Text("• LRU (Least Recently Used)", font_size=18, color=BLUE)
            lfu = Text("• LFU (Least Frequently Used)", font_size=18, color=BLUE)
            fifo = Text("• FIFO (First In First Out)", font_size=18, color=BLUE)
            
            policies = VGroup(lru, lfu, fifo).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            policies.next_to(evict_title, DOWN, buff=0.4)
            
            self.play(Write(evict_title))
            self.play(Write(lru))
            self.wait(0.3)
            self.play(Write(lfu))
            self.wait(0.3)
            self.play(Write(fifo))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def cdn_explanation(self):
        with self.voiceover(text="Chapter Seven: Content Delivery Network. While cache speeds up database queries, we have another performance opportunity: static content. Images, videos, CSS, and JavaScript files don't change often but consume significant bandwidth. This is where CDN comes in.") as tracker:
            chapter_title = Text("Chapter 7: CDN", font_size=40, color=BLUE)
            subtitle = Text("Content Delivery Network", font_size=28, color=GRAY)
            title_group = VGroup(chapter_title, subtitle).arrange(DOWN, buff=0.3)
            self.play(Write(chapter_title))
            self.play(Write(subtitle))
            self.wait(1)
            self.play(FadeOut(title_group))
        
        with self.voiceover(text="A CDN is a network of geographically dispersed servers used to deliver static content. CDN servers cache static content like images, videos, CSS, and JavaScript files. When a user requests a file, it's served from the nearest CDN server instead of your origin server.") as tracker:
            # World map representation
            map_outline = Rectangle(height=3.5, width=6.5, color=BLUE, fill_opacity=0.1)
            map_label = Text("Global CDN Network", font_size=24, color=BLUE).next_to(map_outline, UP, buff=0.3)
            
            self.play(Create(map_outline), Write(map_label))
            
            # CDN server locations
            cdn1 = self.create_server_icon(scale=0.4).shift(LEFT * 2.5 + UP * 1)
            cdn1_label = Text("US West", font_size=12).next_to(cdn1, DOWN, buff=0.1)
            
            cdn2 = self.create_server_icon(scale=0.4).shift(LEFT * 0.5 + UP * 0.5)
            cdn2_label = Text("US East", font_size=12).next_to(cdn2, DOWN, buff=0.1)
            
            cdn3 = self.create_server_icon(scale=0.4).shift(RIGHT * 1.5 + UP * 1.2)
            cdn3_label = Text("Europe", font_size=12).next_to(cdn3, DOWN, buff=0.1)
            
            cdn4 = self.create_server_icon(scale=0.4).shift(RIGHT * 2.8 + DOWN * 0.3)
            cdn4_label = Text("Asia", font_size=12).next_to(cdn4, DOWN, buff=0.1)
            
            cdn5 = self.create_server_icon(scale=0.4).shift(LEFT * 1.5 + DOWN * 1)
            cdn5_label = Text("S. America", font_size=12).next_to(cdn5, DOWN, buff=0.1)
            
            self.play(
                FadeIn(cdn1), Write(cdn1_label),
                FadeIn(cdn2), Write(cdn2_label),
                FadeIn(cdn3), Write(cdn3_label),
                FadeIn(cdn4), Write(cdn4_label),
                FadeIn(cdn5), Write(cdn5_label)
            )
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Here's a practical example. User A in San Francisco requests image dot png. The request goes to the nearby CDN server. If the CDN has the file cached, it returns it immediately - say in 30 milliseconds. Compare this to fetching from the origin server in New York, which might take 120 milliseconds. That's four times faster!") as tracker:
            example_title = Text("CDN Performance Example", font_size=32, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(example_title))
            
            # User in San Francisco
            user = self.create_user_icon().shift(LEFT * 5 + UP * 0.5)
            user_label = Text("User A\n(San Francisco)", font_size=16, color=WHITE).next_to(user, DOWN, buff=0.2)
            request = Text("image.png", font_size=14, color=YELLOW).next_to(user, UP, buff=0.2)
            
            self.play(FadeIn(user), Write(user_label), Write(request))
            
            # CDN Server
            cdn_server = self.create_server_icon(scale=0.6).shift(LEFT * 0.5 + UP * 0.5)
            cdn_label = Text("CDN Server\n(West Coast)", font_size=16, color=ORANGE).next_to(cdn_server, DOWN, buff=0.3)
            
            self.play(FadeIn(cdn_server), Write(cdn_label))
            
            # Fast path
            fast_arrow = Arrow(user.get_right(), cdn_server.get_left(), color=GREEN, buff=0.2, stroke_width=5)
            fast_label = Text("30ms ⚡", font_size=20, color=GREEN, weight=BOLD).next_to(fast_arrow, UP, buff=0.1)
            
            self.play(Create(fast_arrow), Write(fast_label))
            self.wait(1)
            
            # Origin Server (for comparison)
            origin_server = self.create_server_icon(scale=0.6).shift(RIGHT * 4.5 + UP * 0.5)
            origin_label = Text("Origin Server\n(New York)", font_size=16, color=BLUE).next_to(origin_server, DOWN, buff=0.3)
            
            self.play(FadeIn(origin_server), Write(origin_label))
            
            # Slow path
            slow_arrow = Arrow(user.get_right() + DOWN * 0.3, origin_server.get_left(), color=RED, buff=0.2, stroke_width=3)
            slow_label = Text("120ms 🐌", font_size=20, color=RED).next_to(slow_arrow, DOWN, buff=0.1)
            
            self.play(Create(slow_arrow), Write(slow_label))
            
            comparison = Text("4x Faster with CDN!", font_size=24, color=GREEN, weight=BOLD).shift(DOWN * 2.5)
            self.play(Write(comparison))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let's understand the CDN workflow. Step one: User requests an image from the CDN URL. Step two: If the CDN server doesn't have the image, it's a cache miss. Step three: The CDN requests the file from the origin server. Step four: The origin returns the file with an optional HTTP header called Time To Live, or TTL, which tells the CDN how long to cache it.") as tracker:
            workflow_title = Text("CDN Workflow", font_size=36, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(workflow_title))
            
            # User
            user = self.create_user_icon().shift(LEFT * 5)
            user_label = Text("User", font_size=16).next_to(user, DOWN, buff=0.2)
            
            # CDN
            cdn = Rectangle(height=1.5, width=2, color=ORANGE, fill_opacity=0.4).shift(LEFT * 1)
            cdn_text = Text("CDN", font_size=20).move_to(cdn.get_center())
            
            # Origin
            origin = Rectangle(height=1.5, width=2, color=BLUE, fill_opacity=0.4).shift(RIGHT * 3.5)
            origin_text = Text("Origin\nServer", font_size=18).move_to(origin.get_center())
            
            self.play(
                FadeIn(user), Write(user_label),
                Create(cdn), Write(cdn_text),
                Create(origin), Write(origin_text)
            )
            
            # Step 1: Request
            step1 = Text("1. Request image", font_size=20, color=YELLOW).shift(UP * 2.2)
            req_arrow = Arrow(user.get_right(), cdn.get_left(), color=YELLOW, buff=0.2)
            req_url = Text("cdn.example.com/image.png", font_size=12, color=YELLOW).next_to(req_arrow, UP, buff=0.1)
            
            self.play(Write(step1))
            self.play(Create(req_arrow), Write(req_url))
            self.wait(1)
            
            # Step 2: Cache Miss
            self.play(FadeOut(step1))
            step2 = Text("2. Cache MISS", font_size=20, color=RED).shift(UP * 2.2)
            miss = Text("✗", font_size=40, color=RED).next_to(cdn, UP, buff=0.2)
            
            self.play(Write(step2), Write(miss))
            self.wait(1)
            
            # Step 3: CDN requests from origin
            self.play(FadeOut(step2))
            step3 = Text("3. CDN → Origin request", font_size=20, color=BLUE).shift(UP * 2.2)
            cdn_to_origin = Arrow(cdn.get_right(), origin.get_left(), color=BLUE, buff=0.2)
            
            self.play(Write(step3))
            self.play(Create(cdn_to_origin))
            self.wait(1)
            
            # Step 4: Origin returns with TTL
            self.play(FadeOut(step3))
            step4 = Text("4. Return with TTL", font_size=20, color=GREEN).shift(UP * 2.2)
            return_arrow = Arrow(origin.get_left(), cdn.get_right(), color=GREEN, buff=0.2)
            ttl_label = Text("TTL: 86400s (1 day)", font_size=12, color=GREEN).next_to(return_arrow, DOWN, buff=0.1)
            
            self.play(Write(step4))
            self.play(Create(return_arrow), Write(ttl_label))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Step five: The CDN caches the file and returns it to the user. Step six: Now when another user requests the same file, it's a cache hit! The CDN serves it directly without contacting the origin. This remains cached until the TTL expires. Popular CDN providers include Amazon CloudFront, Akamai, and Cloudflare.") as tracker:
            workflow_title = Text("CDN Workflow (continued)", font_size=36, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(workflow_title))
            
            # Setup again
            user1 = self.create_user_icon().shift(LEFT * 5 + UP * 1)
            user1_label = Text("User 1", font_size=14).next_to(user1, DOWN, buff=0.15)
            
            user2 = self.create_user_icon().shift(LEFT * 5 + DOWN * 1)
            user2_label = Text("User 2", font_size=14).next_to(user2, DOWN, buff=0.15)
            
            cdn = Rectangle(height=1.8, width=2, color=ORANGE, fill_opacity=0.4).shift(RIGHT * 0.5)
            cdn_text = Text("CDN", font_size=20).move_to(cdn.get_center())
            cached = Text("✓ Cached", font_size=14, color=GREEN).next_to(cdn, UP, buff=0.2)
            
            origin = Rectangle(height=1.5, width=2, color=BLUE, fill_opacity=0.4).shift(RIGHT * 4.5)
            origin_text = Text("Origin", font_size=18).move_to(origin.get_center())
            
            self.play(
                FadeIn(user1), Write(user1_label),
                FadeIn(user2), Write(user2_label),
                Create(cdn), Write(cdn_text), Write(cached),
                Create(origin), Write(origin_text)
            )
            
            # Cache hit for user 2
            hit_arrow = Arrow(user2.get_right(), cdn.get_left() + DOWN * 0.3, color=GREEN, buff=0.2, stroke_width=5)
            hit_label = Text("Cache HIT! ⚡", font_size=18, color=GREEN, weight=BOLD).next_to(hit_arrow, DOWN, buff=0.1)
            
            return_fast = Arrow(cdn.get_left() + DOWN * 0.3, user2.get_right(), color=GREEN, buff=0.2, stroke_width=5)
            
            self.play(Create(hit_arrow), Write(hit_label))
            self.play(Create(return_fast))
            
            no_origin = Text("✗ No origin request needed", font_size=16, color=GREEN).shift(DOWN * 2.5)
            self.play(Write(no_origin))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Here are example CDN URLs. Amazon CloudFront URLs look like this with a unique identifier. Akamai uses a similar pattern. Your static assets are accessed through these CDN URLs instead of your origin domain.") as tracker:
            url_title = Text("CDN URL Examples", font_size=32, color=ORANGE).to_edge(UP, buff=0.5)
            self.play(Write(url_title))
            
            example1 = Text("Amazon CloudFront:", font_size=22, color=BLUE).shift(UP * 1.2)
            url1 = Text("https://d111111abcdef8.cloudfront.net/logo.jpg", font_size=16, color=GRAY)
            url1.next_to(example1, DOWN, buff=0.3)
            
            example2 = Text("Akamai:", font_size=22, color=BLUE).shift(DOWN * 0.5)
            url2 = Text("https://example.akamaized.net/images/photo.png", font_size=16, color=GRAY)
            url2.next_to(example2, DOWN, buff=0.3)
            
            self.play(Write(example1))
            self.play(Write(url1))
            self.wait(1)
            self.play(Write(example2))
            self.play(Write(url2))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def stateless_web_tier(self):
        with self.voiceover(text="Chapter Eight: Stateless Web Tier. As we continue scaling, we need to address session state management. Now we move state data out of the web tier. A stateless web tier is critical for horizontal scaling.") as tracker:
            chapter_title = Text("Chapter 8: Stateless Web Tier", font_size=40, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="First, let's understand stateful architecture. In a stateful setup, the server remembers client data between requests. For example, user A's session is stored on Server 1. User A must always be routed to Server 1. This is called sticky sessions, and it's a problem.") as tracker:
            stateful_title = Text("Stateful Architecture", font_size=32, color=RED).to_edge(UP, buff=0.5)
            problem = Text("❌ Problem: Sticky Sessions", font_size=20, color=RED).next_to(stateful_title, DOWN, buff=0.3)
            
            self.play(Write(stateful_title), Write(problem))
            
            # Users
            userA = self.create_user_icon().shift(LEFT * 5 + UP * 1.5)
            userA_label = Text("User A", font_size=16, color=BLUE).next_to(userA, DOWN, buff=0.2)
            
            userB = self.create_user_icon().shift(LEFT * 5 + DOWN * 1.5)
            userB_label = Text("User B", font_size=16, color=GREEN).next_to(userB, DOWN, buff=0.2)
            
            # Servers with state
            server1 = Rectangle(height=2, width=2, color=BLUE, fill_opacity=0.4).shift(RIGHT * 2 + UP * 1.5)
            server1_label = Text("Server 1", font_size=18).move_to(server1.get_top() + DOWN * 0.3)
            session_a = Text("Session A\n(User A data)", font_size=14, color=BLUE).move_to(server1.get_center() + DOWN * 0.3)
            
            server2 = Rectangle(height=2, width=2, color=GREEN, fill_opacity=0.4).shift(RIGHT * 2 + DOWN * 1.5)
            server2_label = Text("Server 2", font_size=18).move_to(server2.get_top() + DOWN * 0.3)
            session_b = Text("Session B\n(User B data)", font_size=14, color=GREEN).move_to(server2.get_center() + DOWN * 0.3)
            
            self.play(
                FadeIn(userA), Write(userA_label),
                FadeIn(userB), Write(userB_label),
                Create(server1), Write(server1_label), Write(session_a),
                Create(server2), Write(server2_label), Write(session_b)
            )
            
            # Sticky connections
            sticky_a = Arrow(userA.get_right(), server1.get_left(), color=BLUE, buff=0.2, stroke_width=4)
            sticky_label_a = Text("MUST use\nServer 1", font_size=12, color=BLUE).next_to(sticky_a, UP, buff=0.1)
            
            sticky_b = Arrow(userB.get_right(), server2.get_left(), color=GREEN, buff=0.2, stroke_width=4)
            sticky_label_b = Text("MUST use\nServer 2", font_size=12, color=GREEN).next_to(sticky_b, DOWN, buff=0.1)
            
            self.play(Create(sticky_a), Write(sticky_label_a))
            self.play(Create(sticky_b), Write(sticky_label_b))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Stateful architecture creates serious problems. If Server 1 fails, User A loses their session and must log in again. Adding or removing servers is difficult because sessions are tied to specific servers. Load balancing is challenging and inefficient. We need a better solution!") as tracker:
            problems_title = Text("Stateful Problems", font_size=36, color=RED).to_edge(UP, buff=0.5)
            self.play(Write(problems_title))
            
            problem1 = Text("❌ Server failure = Lost sessions", font_size=22, color=RED)
            problem1.shift(UP * 1.2)
            
            problem2 = Text("❌ Hard to add/remove servers", font_size=22, color=RED)
            problem2.shift(UP * 0.2)
            
            problem3 = Text("❌ Inefficient load balancing", font_size=22, color=RED)
            problem3.shift(DOWN * 0.8)
            
            problem4 = Text("❌ Can't scale easily", font_size=22, color=RED)
            problem4.shift(DOWN * 1.8)
            
            self.play(Write(problem1))
            self.wait(0.7)
            self.play(Write(problem2))
            self.wait(0.7)
            self.play(Write(problem3))
            self.wait(0.7)
            self.play(Write(problem4))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now let's look at stateless architecture. This is the solution! In stateless architecture, web servers don't store any session data. Instead, session data is stored in a shared data store accessible by all web servers. This is typically a NoSQL database like Redis or Memcached.") as tracker:
            stateless_title = Text("Stateless Architecture", font_size=32, color=GREEN).to_edge(UP, buff=0.5)
            solution = Text("✓ Solution: Shared Session Storage", font_size=20, color=GREEN).next_to(stateless_title, DOWN, buff=0.3)
            
            self.play(Write(stateless_title), Write(solution))
            
            # Users
            userA = self.create_user_icon().shift(LEFT * 5.5 + UP * 1.5)
            userA_label = Text("User A", font_size=16).next_to(userA, DOWN, buff=0.2)
            
            userB = self.create_user_icon().shift(LEFT * 5.5 + DOWN * 1.5)
            userB_label = Text("User B", font_size=16).next_to(userB, DOWN, buff=0.2)
            
            # Stateless servers
            server1 = Rectangle(height=1.5, width=1.8, color=GREEN, fill_opacity=0.3).shift(LEFT * 1.5 + UP * 1.5)
            server1_label = Text("Server 1", font_size=16).move_to(server1.get_center())
            no_state1 = Text("No state", font_size=12, color=GRAY).next_to(server1, DOWN, buff=0.15)
            
            server2 = Rectangle(height=1.5, width=1.8, color=GREEN, fill_opacity=0.3).shift(LEFT * 1.5 + DOWN * 1.5)
            server2_label = Text("Server 2", font_size=16).move_to(server2.get_center())
            no_state2 = Text("No state", font_size=12, color=GRAY).next_to(server2, DOWN, buff=0.15)
            
            server3 = Rectangle(height=1.5, width=1.8, color=GREEN, fill_opacity=0.3).shift(RIGHT * 1.2 + UP * 1.5)
            server3_label = Text("Server 3", font_size=16).move_to(server3.get_center())
            no_state3 = Text("No state", font_size=12, color=GRAY).next_to(server3, DOWN, buff=0.15)
            
            # Shared session store
            session_store = Rectangle(height=2.5, width=2.5, color=ORANGE, fill_opacity=0.5).shift(RIGHT * 4.5)
            store_label = Text("Session\nStore", font_size=20, color=WHITE, weight=BOLD).move_to(session_store.get_center())
            store_tech = Text("(Redis/NoSQL)", font_size=14, color=GRAY).next_to(session_store, DOWN, buff=0.2)
            
            sessions = Text("All Sessions:\nUser A, User B, ...", font_size=12, color=YELLOW).move_to(session_store.get_center() + DOWN * 0.6)
            
            self.play(
                FadeIn(userA), Write(userA_label),
                FadeIn(userB), Write(userB_label),
                Create(server1), Write(server1_label), Write(no_state1),
                Create(server2), Write(server2_label), Write(no_state2),
                Create(server3), Write(server3_label), Write(no_state3)
            )
            
            self.play(Create(session_store), Write(store_label), Write(store_tech), Write(sessions))
            
            # Flexible routing
            route1 = Arrow(userA.get_right(), server1.get_left(), color=BLUE, buff=0.1, stroke_width=2)
            route2 = Arrow(userB.get_right(), server3.get_left(), color=GREEN, buff=0.1, stroke_width=2)
            
            self.play(Create(route1), Create(route2))
            
            # All servers can access session store
            access1 = Arrow(server1.get_right(), session_store.get_left() + UP * 0.5, color=YELLOW, buff=0.1, stroke_width=2)
            access2 = Arrow(server2.get_right(), session_store.get_left(), color=YELLOW, buff=0.1, stroke_width=2)
            access3 = Arrow(server3.get_right(), session_store.get_left() + DOWN * 0.5, color=YELLOW, buff=0.1, stroke_width=2)
            
            self.play(Create(access1), Create(access2), Create(access3))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="The benefits are enormous! Any user can connect to any server because session data is centralized. Servers become truly interchangeable. We can add or remove servers dynamically based on traffic. Autoscaling becomes possible. The load balancer can distribute traffic evenly without worrying about sessions. This is true horizontal scaling!") as tracker:
            benefits_title = Text("Stateless Benefits", font_size=36, color=GREEN).to_edge(UP, buff=0.5)
            self.play(Write(benefits_title))
            
            benefit1 = Text("✓ Any user → Any server", font_size=24, color=GREEN)
            benefit1.shift(UP * 1.4)
            
            benefit2 = Text("✓ Servers are interchangeable", font_size=24, color=GREEN)
            benefit2.shift(UP * 0.6)
            
            benefit3 = Text("✓ Easy to add/remove servers", font_size=24, color=GREEN)
            benefit3.shift(DOWN * 0.2)
            
            benefit4 = Text("✓ Autoscaling enabled!", font_size=24, color=GREEN)
            benefit4.shift(DOWN * 1.0)
            
            benefit5 = Text("✓ True horizontal scaling", font_size=24, color=YELLOW, weight=BOLD)
            benefit5.shift(DOWN * 1.8)
            
            self.play(Write(benefit1))
            self.wait(0.5)
            self.play(Write(benefit2))
            self.wait(0.5)
            self.play(Write(benefit3))
            self.wait(0.5)
            self.play(Write(benefit4))
            self.wait(0.5)
            self.play(Write(benefit5))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Here's how autoscaling works with a stateless web tier. We monitor traffic with a graph showing requests per second. When traffic increases, we automatically spin up more servers. When traffic decreases, we remove servers to save costs. This is only possible because our servers are stateless!") as tracker:
            autoscale_title = Text("Autoscaling in Action", font_size=32, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(autoscale_title))
            
            # Traffic graph
            axes = Axes(
                x_range=[0, 10, 2],
                y_range=[0, 100, 20],
                x_length=8,
                y_length=3,
                axis_config={"color": BLUE, "include_numbers": False}
            ).shift(DOWN * 0.3)
            
            x_label = Text("Time", font_size=16).next_to(axes, DOWN, buff=0.2)
            y_label = Text("Traffic", font_size=16).next_to(axes, LEFT, buff=0.2)
            
            # Traffic curve
            traffic_curve = axes.plot(lambda x: 30 + 50 * np.sin(x * 0.8), color=ORANGE)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            self.play(Create(traffic_curve))
            
            # Server count indicator
            low_traffic = Text("Low Traffic\n→ 2 servers", font_size=16, color=GREEN).shift(LEFT * 4 + DOWN * 2.5)
            high_traffic = Text("High Traffic\n→ 8 servers", font_size=16, color=RED).shift(RIGHT * 2 + DOWN * 2.5)
            
            self.play(Write(low_traffic))
            self.wait(1)
            self.play(Write(high_traffic))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def multiple_data_centers(self):
        with self.voiceover(text="Chapter Nine: Multiple Data Centers. To truly serve a global user base, we need multiple data centers across different geographical regions. This improves availability and provides better user experience for users worldwide.") as tracker:
            chapter_title = Text("Chapter 9: Multiple Data Centers", font_size=38, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="Here's a multi-datacenter setup. We have one datacenter on the US East Coast and another on the US West Coast. Users are automatically routed to the nearest datacenter based on their geographic location. This is done using geo DNS, which returns different IP addresses based on the user's location.") as tracker:
            # World map outline
            map_box = Rectangle(height=4, width=7, color=BLUE, fill_opacity=0.05).shift(UP * 0.3)
            
            self.play(Create(map_box))
            
            # Data Center 1 - US East
            dc1_box = Rectangle(height=1.5, width=2, color=GREEN, fill_opacity=0.4).shift(LEFT * 2 + UP * 0.5)
            dc1_label = Text("Data Center 1", font_size=18, color=WHITE).move_to(dc1_box.get_top() + DOWN * 0.25)
            dc1_location = Text("US-East", font_size=14, color=GREEN).next_to(dc1_box, DOWN, buff=0.15)
            
            # Data Center 2 - US West
            dc2_box = Rectangle(height=1.5, width=2, color=ORANGE, fill_opacity=0.4).shift(RIGHT * 2.5 + UP * 0.5)
            dc2_label = Text("Data Center 2", font_size=18, color=WHITE).move_to(dc2_box.get_top() + DOWN * 0.25)
            dc2_location = Text("US-West", font_size=14, color=ORANGE).next_to(dc2_box, DOWN, buff=0.15)
            
            self.play(
                Create(dc1_box), Write(dc1_label), Write(dc1_location),
                Create(dc2_box), Write(dc2_label), Write(dc2_location)
            )
            
            # Users
            user_east = self.create_user_icon().shift(LEFT * 5 + UP * 0.5)
            user_east_label = Text("East Coast\nUser", font_size=14).next_to(user_east, DOWN, buff=0.2)
            
            user_west = self.create_user_icon().shift(RIGHT * 6 + UP * 0.5)
            user_west_label = Text("West Coast\nUser", font_size=14).next_to(user_west, DOWN, buff=0.2)
            
            self.play(
                FadeIn(user_east), Write(user_east_label),
                FadeIn(user_west), Write(user_west_label)
            )
            
            # Routing
            route_east = Arrow(user_east.get_right(), dc1_box.get_left(), color=GREEN, buff=0.2, stroke_width=4)
            route_west = Arrow(user_west.get_left(), dc2_box.get_right(), color=ORANGE, buff=0.2, stroke_width=4)
            
            self.play(Create(route_east), Create(route_west))
            
            # Traffic percentages
            traffic1 = Text("x% traffic", font_size=16, color=GREEN).next_to(dc1_box, UP, buff=0.3)
            traffic2 = Text("(100-x)% traffic", font_size=16, color=ORANGE).next_to(dc2_box, UP, buff=0.3)
            
            self.play(Write(traffic1), Write(traffic2))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now imagine Data Center 2 on the West Coast goes offline due to a power outage or network issue. The GeoDNS routing system detects this failure immediately and reroutes all traffic to Data Center 1. One hundred percent of traffic now flows to the East Coast datacenter. Users experience minimal disruption.") as tracker:
            failover_title = Text("Data Center Failover", font_size=32, color=RED).to_edge(UP, buff=0.5)
            self.play(Write(failover_title))
            
            # Normal state first
            dc1_box = Rectangle(height=1.5, width=2.2, color=GREEN, fill_opacity=0.4).shift(LEFT * 3)
            dc1_label = Text("DC1 US-East", font_size=18, color=WHITE).move_to(dc1_box.get_center())
            dc1_status = Text("✓ ONLINE", font_size=14, color=GREEN, weight=BOLD).next_to(dc1_box, UP, buff=0.2)
            
            dc2_box = Rectangle(height=1.5, width=2.2, color=ORANGE, fill_opacity=0.4).shift(RIGHT * 3)
            dc2_label = Text("DC2 US-West", font_size=18, color=WHITE).move_to(dc2_box.get_center())
            dc2_status = Text("✓ ONLINE", font_size=14, color=ORANGE).next_to(dc2_box, UP, buff=0.2)
            
            self.play(
                Create(dc1_box), Write(dc1_label), Write(dc1_status),
                Create(dc2_box), Write(dc2_label), Write(dc2_status)
            )
            self.wait(0.5)
            
            # DC2 fails
            dc2_failed = Rectangle(height=1.5, width=2.2, color=RED, fill_opacity=0.6).shift(RIGHT * 3)
            dc2_failed_status = Text("✗ OFFLINE", font_size=14, color=RED, weight=BOLD).next_to(dc2_failed, UP, buff=0.2)
            x_mark = Text("✗", font_size=60, color=RED).move_to(dc2_failed.get_center())
            
            self.play(
                Transform(dc2_box, dc2_failed),
                Transform(dc2_status, dc2_failed_status),
                Write(x_mark)
            )
            self.wait(1)
            
            # Traffic reroute
            users = VGroup(
                self.create_user_icon().shift(LEFT * 6 + UP * 1),
                self.create_user_icon().shift(LEFT * 6),
                self.create_user_icon().shift(LEFT * 6 + DOWN * 1)
            )
            
            self.play(FadeIn(users))
            
            reroute_arrows = VGroup(
                Arrow(users[0].get_right(), dc1_box.get_left() + UP * 0.3, color=YELLOW, buff=0.2, stroke_width=3),
                Arrow(users[1].get_right(), dc1_box.get_left(), color=YELLOW, buff=0.2, stroke_width=3),
                Arrow(users[2].get_right(), dc1_box.get_left() + DOWN * 0.3, color=YELLOW, buff=0.2, stroke_width=3)
            )
            
            self.play(Create(reroute_arrows))
            
            traffic_label = Text("100% → DC1", font_size=22, color=YELLOW, weight=BOLD).shift(DOWN * 2.5)
            self.play(Write(traffic_label))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Setting up multiple data centers introduces several technical challenges we must address. First challenge: traffic redirection. We need GeoDNS to route users to the correct datacenter. GeoDNS is a DNS service that returns different IP addresses based on where the user is located.") as tracker:
            challenges_title = Text("Multi-DC Technical Challenges", font_size=32, color=ORANGE).to_edge(UP, buff=0.5)
            self.play(Write(challenges_title))
            
            # Challenge 1: Traffic Redirection
            challenge1_num = Text("1", font_size=40, color=BLUE).shift(LEFT * 5 + UP * 0.8)
            challenge1_title = Text("Traffic Redirection", font_size=26, color=BLUE).next_to(challenge1_num, RIGHT, buff=0.4)
            challenge1_desc = Text("GeoDNS routes based on location", font_size=18, color=GRAY).next_to(challenge1_title, DOWN, buff=0.25, aligned_edge=LEFT)
            
            # GeoDNS diagram
            dns = Rectangle(height=0.8, width=1.5, color=PURPLE, fill_opacity=0.4).shift(RIGHT * 1.5 + UP * 1)
            dns_label = Text("GeoDNS", font_size=14).move_to(dns.get_center())
            
            user1 = self.create_user_icon(scale=0.3).shift(RIGHT * 4 + UP * 1.5)
            loc1 = Text("NYC", font_size=10).next_to(user1, RIGHT, buff=0.1)
            ip1 = Text("IP: 1.2.3.4", font_size=10, color=GREEN).next_to(user1, DOWN, buff=0.1)
            
            user2 = self.create_user_icon(scale=0.3).shift(RIGHT * 4 + UP * 0.5)
            loc2 = Text("LA", font_size=10).next_to(user2, RIGHT, buff=0.1)
            ip2 = Text("IP: 5.6.7.8", font_size=10, color=ORANGE).next_to(user2, DOWN, buff=0.1)
            
            self.play(Write(challenge1_num), Write(challenge1_title))
            self.play(Write(challenge1_desc))
            self.play(
                Create(dns), Write(dns_label),
                FadeIn(user1), Write(loc1), Write(ip1),
                FadeIn(user2), Write(loc2), Write(ip2)
            )
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Second challenge: data synchronization. Users from different regions could access the same resources - like their profile or posts. We need to replicate data across regions. A common strategy is to use database replication with eventual consistency. Changes in one datacenter propagate to others, though not instantly.") as tracker:
            challenges_title = Text("Challenge 2: Data Synchronization", font_size=32, color=ORANGE).to_edge(UP, buff=0.5)
            self.play(Write(challenges_title))
            
            # Two datacenters with databases
            dc1 = Rectangle(height=2, width=2.5, color=GREEN, fill_opacity=0.3).shift(LEFT * 3.5)
            dc1_label = Text("DC1", font_size=18).move_to(dc1.get_top() + DOWN * 0.3)
            db1 = self.create_database_icon(color=GREEN, scale=0.5).move_to(dc1.get_center() + DOWN * 0.3)
            
            dc2 = Rectangle(height=2, width=2.5, color=ORANGE, fill_opacity=0.3).shift(RIGHT * 3.5)
            dc2_label = Text("DC2", font_size=18).move_to(dc2.get_top() + DOWN * 0.3)
            db2 = self.create_database_icon(color=ORANGE, scale=0.5).move_to(dc2.get_center() + DOWN * 0.3)
            
            self.play(
                Create(dc1), Write(dc1_label), FadeIn(db1),
                Create(dc2), Write(dc2_label), FadeIn(db2)
            )
            
            # Bi-directional replication
            repl_right = Arrow(db1.get_right(), db2.get_left(), color=BLUE, buff=0.2, stroke_width=3)
            repl_left = Arrow(db2.get_left(), db1.get_right(), color=BLUE, buff=0.2, stroke_width=3)
            repl_left.shift(DOWN * 0.15)
            repl_right.shift(UP * 0.15)
            
            sync_label = Text("Bi-directional\nReplication", font_size=16, color=BLUE).shift(DOWN * 1.8)
            
            self.play(Create(repl_right), Create(repl_left))
            self.play(Write(sync_label))
            
            consistency = Text("Eventual Consistency", font_size=18, color=YELLOW, weight=BOLD).shift(DOWN * 2.8)
            self.play(Write(consistency))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Third challenge: testing and deployment. With multiple data centers, testing becomes more complex. You need to test in all regions. Automated deployment pipelines are essential. You want to deploy updates to all datacenters simultaneously or in a controlled rollout. Monitoring and rollback capabilities are critical.") as tracker:
            challenges_title = Text("Challenge 3: Testing & Deployment", font_size=32, color=ORANGE).to_edge(UP, buff=0.5)
            self.play(Write(challenges_title))
            
            test_icon = Text("🧪", font_size=50).shift(LEFT * 3 + UP * 0.8)
            test_title = Text("Comprehensive Testing", font_size=24, color=BLUE).next_to(test_icon, RIGHT, buff=0.5)
            test_items = VGroup(
                Text("• Test in all regions", font_size=16),
                Text("• Network latency tests", font_size=16),
                Text("• Failover scenarios", font_size=16)
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(test_title, DOWN, buff=0.3, aligned_edge=LEFT)
            
            self.play(Write(test_icon), Write(test_title))
            self.play(Write(test_items))
            self.wait(1.5)
            
            deploy_icon = Text("🚀", font_size=50).shift(LEFT * 3 + DOWN * 1.5)
            deploy_title = Text("Automated Deployment", font_size=24, color=GREEN).next_to(deploy_icon, RIGHT, buff=0.5)
            deploy_items = VGroup(
                Text("• CI/CD pipelines", font_size=16),
                Text("• Synchronized rollouts", font_size=16),
                Text("• Quick rollback", font_size=16)
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(deploy_title, DOWN, buff=0.3, aligned_edge=LEFT)
            
            self.play(Write(deploy_icon), Write(deploy_title))
            self.play(Write(deploy_items))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def message_queue(self):
        with self.voiceover(text="Chapter Ten: Message Queue. As our system grows in complexity, we need better ways to handle asynchronous processing. Enter the message queue - a powerful architecture pattern for building scalable, decoupled systems.") as tracker:
            chapter_title = Text("Chapter 10: Message Queue", font_size=40, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="A message queue is a durable component stored in memory that supports asynchronous communication. It serves as a buffer and distributes tasks to workers. Here's the basic architecture: producers publish messages to the queue, and consumers or workers subscribe to the queue and perform the tasks.") as tracker:
            arch_title = Text("Message Queue Architecture", font_size=30, color=PURPLE).to_edge(UP, buff=0.5)
            self.play(Write(arch_title))
            
            # Producers (Web Servers)
            producer1 = Rectangle(height=1, width=1.5, color=GREEN, fill_opacity=0.4).shift(LEFT * 5 + UP * 1)
            producer1_label = Text("Web\nServer 1", font_size=14).move_to(producer1.get_center())
            
            producer2 = Rectangle(height=1, width=1.5, color=GREEN, fill_opacity=0.4).shift(LEFT * 5 + DOWN * 1)
            producer2_label = Text("Web\nServer 2", font_size=14).move_to(producer2.get_center())
            
            producers_label = Text("Producers", font_size=18, color=GREEN, weight=BOLD).shift(LEFT * 5 + UP * 2.2)
            
            # Message Queue
            queue = Rectangle(height=3, width=2.5, color=PURPLE, fill_opacity=0.5)
            queue_label = Text("Message\nQueue", font_size=20, color=WHITE, weight=BOLD).move_to(queue.get_top() + DOWN * 0.5)
            
            # Messages in queue
            msg1 = Rectangle(height=0.3, width=2, color=YELLOW, fill_opacity=0.7).move_to(queue.get_center() + UP * 0.3)
            msg2 = Rectangle(height=0.3, width=2, color=YELLOW, fill_opacity=0.7).move_to(queue.get_center())
            msg3 = Rectangle(height=0.3, width=2, color=YELLOW, fill_opacity=0.7).move_to(queue.get_center() + DOWN * 0.3)
            messages = VGroup(msg1, msg2, msg3)
            
            buffer_label = Text("Buffer", font_size=14, color=YELLOW).next_to(queue, DOWN, buff=0.2)
            
            # Consumers (Workers)
            consumer1 = Rectangle(height=1, width=1.5, color=ORANGE, fill_opacity=0.4).shift(RIGHT * 5 + UP * 1)
            consumer1_label = Text("Worker 1", font_size=16).move_to(consumer1.get_center())
            
            consumer2 = Rectangle(height=1, width=1.5, color=ORANGE, fill_opacity=0.4).shift(RIGHT * 5 + DOWN * 1)
            consumer2_label = Text("Worker 2", font_size=16).move_to(consumer2.get_center())
            
            consumers_label = Text("Consumers", font_size=18, color=ORANGE, weight=BOLD).shift(RIGHT * 5 + UP * 2.2)
            
            self.play(Write(producers_label))
            self.play(Create(producer1), Write(producer1_label))
            self.play(Create(producer2), Write(producer2_label))
            
            self.play(Create(queue), Write(queue_label), Write(buffer_label))
            self.play(Create(messages))
            
            self.play(Write(consumers_label))
            self.play(Create(consumer1), Write(consumer1_label))
            self.play(Create(consumer2), Write(consumer2_label))
            
            # Arrows showing flow
            publish1 = Arrow(producer1.get_right(), queue.get_left() + UP * 0.5, color=GREEN, buff=0.1, stroke_width=2)
            publish2 = Arrow(producer2.get_right(), queue.get_left() + DOWN * 0.5, color=GREEN, buff=0.1, stroke_width=2)
            
            consume1 = Arrow(queue.get_right() + UP * 0.5, consumer1.get_left(), color=ORANGE, buff=0.1, stroke_width=2)
            consume2 = Arrow(queue.get_right() + DOWN * 0.5, consumer2.get_left(), color=ORANGE, buff=0.1, stroke_width=2)
            
            publish_label = Text("Publish", font_size=12, color=GREEN).next_to(publish1, UP, buff=0.1)
            consume_label = Text("Consume", font_size=12, color=ORANGE).next_to(consume1, UP, buff=0.1)
            
            self.play(Create(publish1), Create(publish2), Write(publish_label))
            self.play(Create(consume1), Create(consume2), Write(consume_label))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let's see a practical example: photo processing. When a user uploads a photo, the web server doesn't process it immediately. Instead, it publishes a job to the message queue with tasks like crop the photo, sharpen it, and apply blur effects. Photo workers pick up these jobs from the queue and process them independently.") as tracker:
            example_title = Text("Example: Photo Processing", font_size=32, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(example_title))
            
            # User uploads photo
            user = self.create_user_icon().shift(LEFT * 6 + UP * 1)
            upload_text = Text("Upload\nphoto.jpg", font_size=14, color=YELLOW).next_to(user, DOWN, buff=0.2)
            
            # Web server
            web_server = Rectangle(height=1.2, width=1.8, color=GREEN, fill_opacity=0.4).shift(LEFT * 3.5 + UP * 1)
            web_label = Text("Web Server", font_size=16).move_to(web_server.get_center())
            
            self.play(FadeIn(user), Write(upload_text))
            self.play(Create(web_server), Write(web_label))
            
            upload_arrow = Arrow(user.get_right(), web_server.get_left(), color=YELLOW, buff=0.2)
            self.play(Create(upload_arrow))
            self.wait(0.5)
            
            # Message queue with jobs
            queue = Rectangle(height=2.5, width=2, color=PURPLE, fill_opacity=0.5).shift(UP * 1)
            queue_label = Text("Queue", font_size=18, color=WHITE).move_to(queue.get_top() + DOWN * 0.35)
            
            job1 = Text("Crop", font_size=14, color=YELLOW).move_to(queue.get_center() + UP * 0.5)
            job2 = Text("Sharpen", font_size=14, color=YELLOW).move_to(queue.get_center())
            job3 = Text("Blur", font_size=14, color=YELLOW).move_to(queue.get_center() + DOWN * 0.5)
            
            self.play(Create(queue), Write(queue_label))
            
            publish_arrow = Arrow(web_server.get_right(), queue.get_left(), color=GREEN, buff=0.1)
            publish_label = Text("Publish Jobs", font_size=12, color=GREEN).next_to(publish_arrow, UP, buff=0.1)
            
            self.play(Create(publish_arrow), Write(publish_label))
            self.play(Write(job1), Write(job2), Write(job3))
            self.wait(1)
            
            # Workers
            worker1 = Rectangle(height=1, width=1.5, color=ORANGE, fill_opacity=0.4).shift(RIGHT * 3.5 + UP * 1.5)
            worker1_label = Text("Worker 1", font_size=14).move_to(worker1.get_center())
            
            worker2 = Rectangle(height=1, width=1.5, color=ORANGE, fill_opacity=0.4).shift(RIGHT * 3.5 + UP * 0.3)
            worker2_label = Text("Worker 2", font_size=14).move_to(worker2.get_center())
            
            worker3 = Rectangle(height=1, width=1.5, color=ORANGE, fill_opacity=0.4).shift(RIGHT * 3.5 + DOWN * 0.9)
            worker3_label = Text("Worker 3", font_size=14).move_to(worker3.get_center())
            
            self.play(
                Create(worker1), Write(worker1_label),
                Create(worker2), Write(worker2_label),
                Create(worker3), Write(worker3_label)
            )
            
            consume_arrows = VGroup(
                Arrow(queue.get_right() + UP * 0.6, worker1.get_left(), color=ORANGE, buff=0.1, stroke_width=2),
                Arrow(queue.get_right() + UP * 0.2, worker2.get_left(), color=ORANGE, buff=0.1, stroke_width=2),
                Arrow(queue.get_right() + DOWN * 0.4, worker3.get_left(), color=ORANGE, buff=0.1, stroke_width=2)
            )
            
            self.play(Create(consume_arrows))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="The beauty of message queues is decoupling. Producers and consumers are completely independent. The web server doesn't wait for photo processing to complete. It returns immediately, giving users a fast response. Workers can be scaled independently. If the queue fills up with many jobs, we can add more workers. If jobs decrease, we remove workers. This is elastic scaling in action!") as tracker:
            benefits_title = Text("Message Queue Benefits", font_size=36, color=PURPLE).to_edge(UP, buff=0.5)
            self.play(Write(benefits_title))
            
            # Benefit 1: Decoupling
            decouple_icon = Text("🔗", font_size=50).shift(LEFT * 3.5 + UP * 1)
            decouple_title = Text("Decoupling", font_size=26, color=BLUE).next_to(decouple_icon, RIGHT, buff=0.5)
            decouple_desc = Text("Producers & consumers\nwork independently", font_size=16, color=GRAY).next_to(decouple_title, DOWN, buff=0.2, aligned_edge=LEFT)
            
            self.play(Write(decouple_icon), Write(decouple_title))
            self.play(Write(decouple_desc))
            self.wait(1.5)
            
            # Benefit 2: Fast response
            fast_icon = Text("⚡", font_size=50).shift(LEFT * 3.5 + DOWN * 0.8)
            fast_title = Text("Fast Response", font_size=26, color=GREEN).next_to(fast_icon, RIGHT, buff=0.5)
            fast_desc = Text("Don't wait for\nprocessing to complete", font_size=16, color=GRAY).next_to(fast_title, DOWN, buff=0.2, aligned_edge=LEFT)
            
            self.play(Write(fast_icon), Write(fast_title))
            self.play(Write(fast_desc))
            self.wait(1.5)
            
            # Benefit 3: Independent scaling
            scale_icon = Text("📊", font_size=50).shift(RIGHT * 1 + UP * 1)
            scale_title = Text("Independent Scaling", font_size=26, color=ORANGE).next_to(scale_icon, RIGHT, buff=0.5)
            scale_desc = VGroup(
                Text("Queue full? → Add workers", font_size=14, color=GREEN),
                Text("Queue empty? → Remove workers", font_size=14, color=RED)
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(scale_title, DOWN, buff=0.2, aligned_edge=LEFT)
            
            self.play(Write(scale_icon), Write(scale_title))
            self.play(Write(scale_desc))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def logging_metrics_automation(self):
        with self.voiceover(text="Chapter Eleven: Logging, Metrics, and Automation. When operating large-scale systems, you cannot rely on manual monitoring. You need comprehensive logging, detailed metrics, and extensive automation. These are the three pillars of operational excellence.") as tracker:
            chapter_title = Text("Chapter 11: Observability & Automation", font_size=36, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="First, let's talk about logging. In a distributed system with hundreds or thousands of servers, you cannot manually check log files on each server. You need centralized logging. Tools like Elasticsearch, Splunk, or CloudWatch aggregate logs from all servers into a single searchable interface. You can search for errors, trace requests across services, and debug issues quickly.") as tracker:
            logging_title = Text("Centralized Logging", font_size=32, color=ORANGE).to_edge(UP, buff=0.5)
            self.play(Write(logging_title))
            
            # Multiple servers producing logs
            server1 = Rectangle(height=0.8, width=1.2, color=GREEN, fill_opacity=0.4).shift(LEFT * 5 + UP * 1.5)
            server1_label = Text("Server 1", font_size=12).move_to(server1.get_center())
            log1 = Text("logs...", font_size=10, color=GRAY).next_to(server1, DOWN, buff=0.1)
            
            server2 = Rectangle(height=0.8, width=1.2, color=GREEN, fill_opacity=0.4).shift(LEFT * 5 + UP * 0.3)
            server2_label = Text("Server 2", font_size=12).move_to(server2.get_center())
            log2 = Text("logs...", font_size=10, color=GRAY).next_to(server2, DOWN, buff=0.1)
            
            server3 = Rectangle(height=0.8, width=1.2, color=GREEN, fill_opacity=0.4).shift(LEFT * 5 + DOWN * 0.9)
            server3_label = Text("Server 3", font_size=12).move_to(server3.get_center())
            log3 = Text("logs...", font_size=10, color=GRAY).next_to(server3, DOWN, buff=0.1)
            
            server_label = Text("100s of Servers", font_size=16, color=WHITE, weight=BOLD).shift(LEFT * 5 + DOWN * 2.2)
            
            self.play(
                Create(server1), Write(server1_label), Write(log1),
                Create(server2), Write(server2_label), Write(log2),
                Create(server3), Write(server3_label), Write(log3)
            )
            self.play(Write(server_label))
            
            # Centralized log system
            log_system = Rectangle(height=2.5, width=3, color=BLUE, fill_opacity=0.4).shift(RIGHT * 2.5)
            log_system_label = Text("Log Aggregation", font_size=18, color=WHITE, weight=BOLD).move_to(log_system.get_top() + DOWN * 0.35)
            
            tools = Text("Elasticsearch\nSplunk\nCloudWatch", font_size=14, color=YELLOW).move_to(log_system.get_center() + DOWN * 0.3)
            
            self.play(Create(log_system), Write(log_system_label), Write(tools))
            
            # Arrows showing log flow
            log_arrows = VGroup(
                Arrow(server1.get_right(), log_system.get_left() + UP * 0.7, color=YELLOW, buff=0.1, stroke_width=2),
                Arrow(server2.get_right(), log_system.get_left(), color=YELLOW, buff=0.1, stroke_width=2),
                Arrow(server3.get_right(), log_system.get_left() + DOWN * 0.7, color=YELLOW, buff=0.1, stroke_width=2)
            )
            
            self.play(Create(log_arrows))
            
            search = Text("🔍 Searchable", font_size=18, color=GREEN, weight=BOLD).next_to(log_system, DOWN, buff=0.3)
            self.play(Write(search))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Second pillar: metrics and monitoring. You need to collect metrics at two levels. Host-level metrics include CPU usage, memory consumption, disk I/O, and network traffic. These tell you about individual server health. Aggregated metrics span across the entire tier - like database performance, cache hit rate, and overall system throughput.") as tracker:
            metrics_title = Text("Metrics & Monitoring", font_size=32, color=GREEN).to_edge(UP, buff=0.5)
            self.play(Write(metrics_title))
            
            # Host-level metrics
            host_title = Text("Host-Level Metrics", font_size=24, color=BLUE).shift(LEFT * 3 + UP * 1.8)
            
            # CPU gauge
            cpu_circle = Circle(radius=0.5, color=RED, fill_opacity=0.3).shift(LEFT * 4.5 + UP * 0.3)
            cpu_label = Text("CPU", font_size=14, color=RED).move_to(cpu_circle.get_center())
            cpu_value = Text("75%", font_size=12, color=RED).next_to(cpu_circle, DOWN, buff=0.15)
            
            # Memory gauge
            mem_circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.3).shift(LEFT * 3 + UP * 0.3)
            mem_label = Text("RAM", font_size=14, color=BLUE).move_to(mem_circle.get_center())
            mem_value = Text("82%", font_size=12, color=BLUE).next_to(mem_circle, DOWN, buff=0.15)
            
            # Disk gauge
            disk_circle = Circle(radius=0.5, color=GREEN, fill_opacity=0.3).shift(LEFT * 1.5 + UP * 0.3)
            disk_label = Text("Disk", font_size=14, color=GREEN).move_to(disk_circle.get_center())
            disk_value = Text("45%", font_size=12, color=GREEN).next_to(disk_circle, DOWN, buff=0.15)
            
            self.play(Write(host_title))
            self.play(
                Create(cpu_circle), Write(cpu_label), Write(cpu_value),
                Create(mem_circle), Write(mem_label), Write(mem_value),
                Create(disk_circle), Write(disk_label), Write(disk_value)
            )
            self.wait(1)
            
            # Aggregated metrics
            agg_title = Text("Aggregated Metrics", font_size=24, color=ORANGE).shift(RIGHT * 2.5 + UP * 1.8)
            
            # Line graph
            axes = Axes(
                x_range=[0, 5, 1],
                y_range=[0, 100, 25],
                x_length=3.5,
                y_length=2,
                axis_config={"include_numbers": False, "color": GRAY}
            ).shift(RIGHT * 2.5 + DOWN * 0.2)
            
            graph = axes.plot(lambda x: 40 + 30 * np.sin(x * 1.5), color=ORANGE)
            graph_label = Text("DB Performance", font_size=12, color=ORANGE).next_to(axes, DOWN, buff=0.2)
            
            self.play(Write(agg_title))
            self.play(Create(axes), Create(graph), Write(graph_label))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="You also need business metrics. These track the health of your product and business. Daily active users, retention rate, and revenue are critical metrics. They help you understand not just if your servers are running, but if your business is healthy. A dashboard displaying all these metrics together gives you complete system visibility.") as tracker:
            business_title = Text("Business Metrics", font_size=32, color=PURPLE).to_edge(UP, buff=0.5)
            self.play(Write(business_title))
            
            # DAU
            dau_box = Rectangle(height=1.2, width=2.5, color=BLUE, fill_opacity=0.3).shift(LEFT * 3.5 + UP * 0.8)
            dau_label = Text("Daily Active Users", font_size=16, color=BLUE).move_to(dau_box.get_top() + DOWN * 0.25)
            dau_value = Text("2.5M", font_size=28, color=BLUE, weight=BOLD).move_to(dau_box.get_center() + DOWN * 0.2)
            dau_trend = Text("↑ 5%", font_size=14, color=GREEN).next_to(dau_value, RIGHT, buff=0.2)
            
            # Retention
            retention_box = Rectangle(height=1.2, width=2.5, color=GREEN, fill_opacity=0.3).shift(LEFT * 3.5 + DOWN * 1)
            retention_label = Text("Retention Rate", font_size=16, color=GREEN).move_to(retention_box.get_top() + DOWN * 0.25)
            retention_value = Text("68%", font_size=28, color=GREEN, weight=BOLD).move_to(retention_box.get_center() + DOWN * 0.2)
            retention_trend = Text("↑ 2%", font_size=14, color=GREEN).next_to(retention_value, RIGHT, buff=0.2)
            
            # Revenue
            revenue_box = Rectangle(height=1.2, width=2.5, color=YELLOW, fill_opacity=0.3).shift(RIGHT * 0.5 + UP * 0.8)
            revenue_label = Text("Revenue", font_size=16, color=YELLOW).move_to(revenue_box.get_top() + DOWN * 0.25)
            revenue_value = Text("$1.2M", font_size=28, color=YELLOW, weight=BOLD).move_to(revenue_box.get_center() + DOWN * 0.2)
            revenue_trend = Text("↑ 8%", font_size=14, color=GREEN).next_to(revenue_value, RIGHT, buff=0.2)
            
            # Conversion
            conversion_box = Rectangle(height=1.2, width=2.5, color=ORANGE, fill_opacity=0.3).shift(RIGHT * 0.5 + DOWN * 1)
            conversion_label = Text("Conversion Rate", font_size=16, color=ORANGE).move_to(conversion_box.get_top() + DOWN * 0.25)
            conversion_value = Text("3.2%", font_size=28, color=ORANGE, weight=BOLD).move_to(conversion_box.get_center() + DOWN * 0.2)
            conversion_trend = Text("↓ 0.5%", font_size=14, color=RED).next_to(conversion_value, RIGHT, buff=0.2)
            
            self.play(
                Create(dau_box), Write(dau_label), Write(dau_value), Write(dau_trend)
            )
            self.wait(0.5)
            self.play(
                Create(retention_box), Write(retention_label), Write(retention_value), Write(retention_trend)
            )
            self.wait(0.5)
            self.play(
                Create(revenue_box), Write(revenue_label), Write(revenue_value), Write(revenue_trend)
            )
            self.wait(0.5)
            self.play(
                Create(conversion_box), Write(conversion_label), Write(conversion_value), Write(conversion_trend)
            )
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Third pillar: automation. For large systems, automation is not optional - it's essential. Continuous Integration means every code commit triggers automated tests. If tests pass, the code is automatically built and ready for deployment. Continuous Deployment takes it further - code that passes all tests is automatically deployed to production. No manual intervention needed!") as tracker:
            automation_title = Text("Automation: The Key to Scale", font_size=32, color=RED).to_edge(UP, buff=0.5)
            self.play(Write(automation_title))
            
            # CI/CD Pipeline
            pipeline_label = Text("CI/CD Pipeline", font_size=24, color=BLUE).shift(UP * 1.8)
            self.play(Write(pipeline_label))
            
            # Step 1: Code commit
            step1 = Rectangle(height=0.8, width=1.5, color=GREEN, fill_opacity=0.4).shift(LEFT * 5 + UP * 0.5)
            step1_label = Text("Code\nCommit", font_size=14).move_to(step1.get_center())
            step1_icon = Text("💻", font_size=20).next_to(step1, UP, buff=0.15)
            
            self.play(Create(step1), Write(step1_label), Write(step1_icon))
            
            # Step 2: Automated tests
            arrow1 = Arrow(step1.get_right(), step1.get_right() + RIGHT * 1, color=BLUE, buff=0)
            step2 = Rectangle(height=0.8, width=1.5, color=BLUE, fill_opacity=0.4).shift(LEFT * 2.8 + UP * 0.5)
            step2_label = Text("Auto\nTests", font_size=14).move_to(step2.get_center())
            step2_icon = Text("🧪", font_size=20).next_to(step2, UP, buff=0.15)
            
            self.play(Create(arrow1))
            self.play(Create(step2), Write(step2_label), Write(step2_icon))
            
            # Step 3: Build
            arrow2 = Arrow(step2.get_right(), step2.get_right() + RIGHT * 1, color=BLUE, buff=0)
            step3 = Rectangle(height=0.8, width=1.5, color=ORANGE, fill_opacity=0.4).shift(LEFT * 0.6 + UP * 0.5)
            step3_label = Text("Build", font_size=14).move_to(step3.get_center())
            step3_icon = Text("🔨", font_size=20).next_to(step3, UP, buff=0.15)
            
            self.play(Create(arrow2))
            self.play(Create(step3), Write(step3_label), Write(step3_icon))
            
            # Step 4: Deploy
            arrow3 = Arrow(step3.get_right(), step3.get_right() + RIGHT * 1, color=BLUE, buff=0)
            step4 = Rectangle(height=0.8, width=1.5, color=RED, fill_opacity=0.4).shift(RIGHT * 1.6 + UP * 0.5)
            step4_label = Text("Deploy", font_size=14).move_to(step4.get_center())
            step4_icon = Text("🚀", font_size=20).next_to(step4, UP, buff=0.15)
            
            self.play(Create(arrow3))
            self.play(Create(step4), Write(step4_label), Write(step4_icon))
            
            # Step 5: Production
            arrow4 = Arrow(step4.get_right(), step4.get_right() + RIGHT * 1, color=BLUE, buff=0)
            step5 = Rectangle(height=0.8, width=1.5, color=GREEN, fill_opacity=0.4).shift(RIGHT * 3.8 + UP * 0.5)
            step5_label = Text("Prod", font_size=14).move_to(step5.get_center())
            step5_icon = Text("✓", font_size=24, color=GREEN, weight=BOLD).next_to(step5, UP, buff=0.1)
            
            self.play(Create(arrow4))
            self.play(Create(step5), Write(step5_label), Write(step5_icon))
            
            # Benefits
            benefit1 = Text("✓ Fast deployments", font_size=18, color=GREEN).shift(DOWN * 1.3)
            benefit2 = Text("✓ Reduced human error", font_size=18, color=GREEN).shift(DOWN * 2)
            benefit3 = Text("✓ Consistent process", font_size=18, color=GREEN).shift(DOWN * 2.7)
            
            self.play(Write(benefit1))
            self.play(Write(benefit2))
            self.play(Write(benefit3))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def database_sharding(self):
        with self.voiceover(text="Chapter Twelve: Database Sharding. As data grows, a single database becomes a bottleneck. Even with replication, the master database can only handle so much write traffic. This is where sharding comes in - one of the most powerful techniques for scaling databases.") as tracker:
            chapter_title = Text("Chapter 12: Database Sharding", font_size=40, color=BLUE)
            self.play(Write(chapter_title))
            self.wait(1)
            self.play(FadeOut(chapter_title))
        
        with self.voiceover(text="First, let's compare our two scaling options. Vertical scaling means upgrading to a more powerful database server. You might go from 16 gigabytes of RAM to 24 terabytes. But there are hard limits, and costs skyrocket. A single server with 24 terabytes of RAM exists but is extremely expensive. This doesn't scale indefinitely.") as tracker:
            compare_title = Text("Database Scaling Strategies", font_size=32, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(compare_title))
            
            # Vertical scaling
            vertical_title = Text("Vertical Scaling", font_size=24, color=ORANGE).shift(LEFT * 3 + UP * 1.5)
            
            db_small = self.create_database_icon(color=ORANGE, scale=0.4).shift(LEFT * 4.5 + UP * 0.3)
            small_label = Text("16 GB RAM", font_size=12, color=GRAY).next_to(db_small, DOWN, buff=0.15)
            
            arrow_up = Arrow(db_small.get_right(), db_small.get_right() + RIGHT * 1.2, color=ORANGE, buff=0, stroke_width=4)
            
            db_large = self.create_database_icon(color=ORANGE, scale=0.7).shift(LEFT * 2 + UP * 0.1)
            large_label = Text("24 TB RAM", font_size=14, color=ORANGE, weight=BOLD).next_to(db_large, DOWN, buff=0.2)
            
            self.play(Write(vertical_title))
            self.play(FadeIn(db_small), Write(small_label))
            self.play(Create(arrow_up))
            self.play(FadeIn(db_large), Write(large_label))
            
            # Problems
            problem1 = Text("❌ Hard limits", font_size=16, color=RED).shift(LEFT * 3 + DOWN * 1.3)
            problem2 = Text("❌ Very expensive", font_size=16, color=RED).shift(LEFT * 3 + DOWN * 1.9)
            problem3 = Text("❌ Single point of failure", font_size=16, color=RED).shift(LEFT * 3 + DOWN * 2.5)
            
            self.play(Write(problem1))
            self.play(Write(problem2))
            self.play(Write(problem3))
            self.wait(1.5)
        
        with self.voiceover(text="Horizontal scaling through sharding is the better solution. Sharding separates large databases into smaller, more manageable parts called shards. Each shard shares the same schema but holds different data. The key is the sharding function, which determines which shard stores which data.") as tracker:
            # Horizontal scaling
            horizontal_title = Text("Horizontal Scaling (Sharding)", font_size=22, color=GREEN).shift(RIGHT * 3 + UP * 1.5)
            
            # Multiple shards
            shard0 = self.create_database_icon(color=GREEN, scale=0.35).shift(RIGHT * 1.5 + UP * 0.5)
            shard0_label = Text("Shard 0", font_size=11, color=GREEN).next_to(shard0, DOWN, buff=0.1)
            
            shard1 = self.create_database_icon(color=GREEN, scale=0.35).shift(RIGHT * 2.8 + UP * 0.5)
            shard1_label = Text("Shard 1", font_size=11, color=GREEN).next_to(shard1, DOWN, buff=0.1)
            
            shard2 = self.create_database_icon(color=GREEN, scale=0.35).shift(RIGHT * 4.1 + UP * 0.5)
            shard2_label = Text("Shard 2", font_size=11, color=GREEN).next_to(shard2, DOWN, buff=0.1)
            
            shard3 = self.create_database_icon(color=GREEN, scale=0.35).shift(RIGHT * 5.4 + UP * 0.5)
            shard3_label = Text("Shard 3", font_size=11, color=GREEN).next_to(shard3, DOWN, buff=0.1)
            
            self.play(Write(horizontal_title))
            self.play(
                FadeIn(shard0), Write(shard0_label),
                FadeIn(shard1), Write(shard1_label),
                FadeIn(shard2), Write(shard2_label),
                FadeIn(shard3), Write(shard3_label)
            )
            
            # Benefits
            benefit1 = Text("✓ Unlimited scaling", font_size=16, color=GREEN).shift(RIGHT * 3 + DOWN * 1.3)
            benefit2 = Text("✓ Cost effective", font_size=16, color=GREEN).shift(RIGHT * 3 + DOWN * 1.9)
            benefit3 = Text("✓ Better performance", font_size=16, color=GREEN).shift(RIGHT * 3 + DOWN * 2.5)
            
            self.play(Write(benefit1))
            self.play(Write(benefit2))
            self.play(Write(benefit3))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let's see how sharding works in practice. We use a hash function to determine which shard stores each user's data. The simplest function is user ID modulo number of shards. For example, with four shards: user ID 0, 4, 8, 12 go to shard 0. User ID 1, 5, 9, 13 go to shard 1. User ID 2, 6, 10, 14 go to shard 2. And user ID 3, 7, 11, 15 go to shard 3.") as tracker:
            sharding_title = Text("Sharding Example: User Database", font_size=30, color=BLUE).to_edge(UP, buff=0.5)
            self.play(Write(sharding_title))
            
            # Hash function
            hash_box = Rectangle(height=1, width=3, color=PURPLE, fill_opacity=0.4).shift(UP * 1.8)
            hash_label = Text("Hash Function", font_size=18, color=WHITE).move_to(hash_box.get_top() + DOWN * 0.25)
            hash_formula = MathTex(r"\text{shard} = \text{user\_id} \bmod 4", font_size=28).move_to(hash_box.get_center() + DOWN * 0.15)
            
            self.play(Create(hash_box), Write(hash_label))
            self.play(Write(hash_formula))
            self.wait(1)
            
            # Shards
            shard0 = Rectangle(height=1.8, width=1.8, color=BLUE, fill_opacity=0.3).shift(LEFT * 4.5 + DOWN * 0.8)
            shard0_title = Text("Shard 0", font_size=16, color=BLUE, weight=BOLD).move_to(shard0.get_top() + DOWN * 0.25)
            shard0_data = Text("Users:\n0, 4, 8\n12, 16...", font_size=12, color=WHITE).move_to(shard0.get_center() + DOWN * 0.25)
            
            shard1 = Rectangle(height=1.8, width=1.8, color=GREEN, fill_opacity=0.3).shift(LEFT * 1.8 + DOWN * 0.8)
            shard1_title = Text("Shard 1", font_size=16, color=GREEN, weight=BOLD).move_to(shard1.get_top() + DOWN * 0.25)
            shard1_data = Text("Users:\n1, 5, 9\n13, 17...", font_size=12, color=WHITE).move_to(shard1.get_center() + DOWN * 0.25)
            
            shard2 = Rectangle(height=1.8, width=1.8, color=ORANGE, fill_opacity=0.3).shift(RIGHT * 1.8 + DOWN * 0.8)
            shard2_title = Text("Shard 2", font_size=16, color=ORANGE, weight=BOLD).move_to(shard2.get_top() + DOWN * 0.25)
            shard2_data = Text("Users:\n2, 6, 10\n14, 18...", font_size=12, color=WHITE).move_to(shard2.get_center() + DOWN * 0.25)
            
            shard3 = Rectangle(height=1.8, width=1.8, color=RED, fill_opacity=0.3).shift(RIGHT * 4.5 + DOWN * 0.8)
            shard3_title = Text("Shard 3", font_size=16, color=RED, weight=BOLD).move_to(shard3.get_top() + DOWN * 0.25)
            shard3_data = Text("Users:\n3, 7, 11\n15, 19...", font_size=12, color=WHITE).move_to(shard3.get_center() + DOWN * 0.25)
            
            self.play(
                Create(shard0), Write(shard0_title), Write(shard0_data),
                Create(shard1), Write(shard1_title), Write(shard1_data),
                Create(shard2), Write(shard2_title), Write(shard2_data),
                Create(shard3), Write(shard3_title), Write(shard3_data)
            )
            
            # Show routing example
            user_example = Text("User 10 → Shard 2", font_size=18, color=ORANGE, weight=BOLD).shift(DOWN * 3)
            calc = Text("10 mod 4 = 2", font_size=14, color=GRAY).next_to(user_example, DOWN, buff=0.2)
            
            self.play(Write(user_example))
            self.play(Write(calc))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Sharding introduces important challenges you must address. First: resharding data. When a shard becomes too large or data distribution is uneven, you need to update the sharding function and move data. This is complex and requires careful planning. Solutions include consistent hashing to minimize data movement.") as tracker:
            challenges_title = Text("Sharding Challenges", font_size=36, color=RED).to_edge(UP, buff=0.5)
            self.play(Write(challenges_title))
            
            # Challenge 1: Resharding
            challenge1_num = Text("1", font_size=40, color=ORANGE).shift(LEFT * 5.5 + UP * 1)
            challenge1_title = Text("Resharding Data", font_size=26, color=ORANGE).next_to(challenge1_num, RIGHT, buff=0.4)
            challenge1_desc = VGroup(
                Text("• Shard becomes too full", font_size=16, color=GRAY),
                Text("• Need to redistribute data", font_size=16, color=GRAY),
                Text("• Requires downtime or careful migration", font_size=16, color=GRAY)
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(challenge1_title, DOWN, buff=0.3, aligned_edge=LEFT)
            
            # Visual: overloaded shard
            normal_shard = Rectangle(height=1, width=1.2, color=GREEN, fill_opacity=0.4).shift(RIGHT * 3 + UP * 1.2)
            normal_label = Text("Normal", font_size=14, color=GREEN).next_to(normal_shard, DOWN, buff=0.1)
            
            full_shard = Rectangle(height=1.5, width=1.2, color=RED, fill_opacity=0.6).shift(RIGHT * 5 + UP * 1)
            full_label = Text("Full!", font_size=14, color=RED, weight=BOLD).next_to(full_shard, DOWN, buff=0.1)
            warning = Text("⚠", font_size=30, color=RED).move_to(full_shard.get_center())
            
            self.play(Write(challenge1_num), Write(challenge1_title))
            self.play(Write(challenge1_desc))
            self.play(
                Create(normal_shard), Write(normal_label),
                Create(full_shard), Write(full_label), Write(warning)
            )
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Second challenge: celebrity or hotspot problem. If a specific shard gets excessive traffic - say all requests for a famous celebrity's posts go to one shard - that shard becomes overwhelmed. You may need to allocate dedicated shards for hot users or use further partitioning strategies.") as tracker:
            challenges_title = Text("Challenge 2: Celebrity Problem", font_size=32, color=RED).to_edge(UP, buff=0.5)
            self.play(Write(challenges_title))
            
            # Show uneven traffic
            shard_a = Rectangle(height=1.2, width=1.5, color=GREEN, fill_opacity=0.3).shift(LEFT * 3 + UP * 0.5)
            shard_a_label = Text("Shard A", font_size=16).move_to(shard_a.get_center())
            traffic_a = Text("Low traffic", font_size=12, color=GREEN).next_to(shard_a, DOWN, buff=0.2)
            
            shard_b = Rectangle(height=1.2, width=1.5, color=RED, fill_opacity=0.6).shift(RIGHT * 1 + UP * 0.5)
            shard_b_label = Text("Shard B", font_size=16).move_to(shard_b.get_center())
            traffic_b = Text("HIGH traffic!", font_size=12, color=RED, weight=BOLD).next_to(shard_b, DOWN, buff=0.2)
            
            celebrity = Text("🌟 Celebrity", font_size=20).next_to(shard_b, UP, buff=0.3)
            
            self.play(
                Create(shard_a), Write(shard_a_label), Write(traffic_a),
                Create(shard_b), Write(shard_b_label), Write(traffic_b)
            )
            self.play(Write(celebrity))
            
            # Traffic visualization
            users_few = VGroup(*[self.create_user_icon(scale=0.2) for _ in range(2)]).arrange(DOWN, buff=0.2).shift(LEFT * 5.5 + UP * 0.5)
            users_many = VGroup(*[self.create_user_icon(scale=0.2) for _ in range(6)]).arrange(DOWN, buff=0.15).shift(LEFT * 2 + UP * 0.3)
            
            arrows_few = VGroup(*[Arrow(u.get_right(), shard_a.get_left(), color=GREEN, buff=0.1, stroke_width=1) for u in users_few])
            arrows_many = VGroup(*[Arrow(u.get_right(), shard_b.get_left(), color=RED, buff=0.1, stroke_width=2) for u in users_many])
            
            self.play(FadeIn(users_few), Create(arrows_few))
            self.play(FadeIn(users_many), Create(arrows_many))
            
            problem = Text("Shard B is overwhelmed!", font_size=18, color=RED, weight=BOLD).shift(DOWN * 2)
            self.play(Write(problem))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Third challenge: join operations and denormalization. Once data is sharded across multiple databases, performing SQL joins becomes very difficult or impossible. You can't easily join data that lives on different servers. The solution is often denormalization - duplicating data across shards to avoid joins. This trades storage space for query performance.") as tracker:
            challenges_title = Text("Challenge 3: Joins & Denormalization", font_size=30, color=ORANGE).to_edge(UP, buff=0.5)
            self.play(Write(challenges_title))
            
            # Problem: Join across shards
            problem_label = Text("Problem: Join across shards", font_size=22, color=RED).shift(UP * 1.8)
            
            shard1_box = Rectangle(height=1.5, width=2, color=BLUE, fill_opacity=0.3).shift(LEFT * 3.5 + UP * 0.3)
            shard1_label = Text("Shard 1", font_size=16).move_to(shard1_box.get_top() + DOWN * 0.25)
            table1 = Text("Users Table", font_size=14, color=BLUE).move_to(shard1_box.get_center() + DOWN * 0.2)
            
            shard2_box = Rectangle(height=1.5, width=2, color=GREEN, fill_opacity=0.3).shift(RIGHT * 3.5 + UP * 0.3)
            shard2_label = Text("Shard 2", font_size=16).move_to(shard2_box.get_top() + DOWN * 0.25)
            table2 = Text("Posts Table", font_size=14, color=GREEN).move_to(shard2_box.get_center() + DOWN * 0.2)
            
            self.play(Write(problem_label))
            self.play(
                Create(shard1_box), Write(shard1_label), Write(table1),
                Create(shard2_box), Write(shard2_label), Write(table2)
            )
            
            join_attempt = Text("JOIN users, posts", font_size=16, color=RED).shift(DOWN * 0.8)
            x_mark = Text("✗ Difficult!", font_size=24, color=RED, weight=BOLD).next_to(join_attempt, DOWN, buff=0.3)
            
            self.play(Write(join_attempt))
            self.play(Write(x_mark))
            self.wait(1.5)
            
            # Solution: Denormalization
            solution_label = Text("Solution: Denormalize", font_size=22, color=GREEN).shift(DOWN * 2.3)
            solution_desc = Text("Duplicate data to avoid joins", font_size=16, color=GRAY).next_to(solution_label, DOWN, buff=0.2)
            
            self.play(Write(solution_label))
            self.play(Write(solution_desc))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="Congratulations! We've completed our journey from a single server to a system capable of serving millions of users. Let's review the essential best practices you must remember when scaling systems.") as tracker:
            conclusion_title = Text("Scaling Best Practices", font_size=40, color=BLUE, weight=BOLD)
            self.play(Write(conclusion_title))
            self.wait(1)
            self.play(FadeOut(conclusion_title))
        
        with self.voiceover(text="Best practice number one: keep the web tier stateless. Store session data in external storage like Redis or NoSQL. This enables true horizontal scaling and easy autoscaling. Number two: build redundancy at every tier. Have multiple web servers, database replicas, cache servers, and data centers. Redundancy prevents single points of failure.") as tracker:
            checklist_title = Text("Essential Practices Checklist", font_size=32, color=GREEN).to_edge(UP, buff=0.4)
            self.play(Write(checklist_title))
            
            practice1 = Text("✓ Keep web tier stateless", font_size=24, color=GREEN)
            practice1.shift(UP * 1.5)
            
            practice2 = Text("✓ Build redundancy at every tier", font_size=24, color=GREEN)
            practice2.shift(UP * 0.8)
            
            self.play(Write(practice1))
            self.wait(1)
            self.play(Write(practice2))
            self.wait(1.5)
        
        with self.voiceover(text="Number three: cache data as much as you can. Caching dramatically reduces database load and improves response times. Use CDNs for static content and in-memory caches for dynamic data. Number four: support multiple data centers. Distribute your system across geographical regions for better availability and lower latency for global users.") as tracker:
            practice3 = Text("✓ Cache data extensively", font_size=24, color=GREEN)
            practice3.shift(UP * 0.1)
            
            practice4 = Text("✓ Support multiple data centers", font_size=24, color=GREEN)
            practice4.shift(DOWN * 0.6)
            
            self.play(Write(practice3))
            self.wait(1)
            self.play(Write(practice4))
            self.wait(1.5)
        
        with self.voiceover(text="Number five: host static assets in CDN. This offloads traffic from your origin servers and provides fast delivery worldwide. Number six: scale your data tier by sharding. When a single database can't handle the load, shard it across multiple databases.") as tracker:
            practice5 = Text("✓ Host static assets in CDN", font_size=24, color=GREEN)
            practice5.shift(DOWN * 1.3)
            
            practice6 = Text("✓ Scale data tier by sharding", font_size=24, color=GREEN)
            practice6.shift(DOWN * 2.0)
            
            self.play(Write(practice5))
            self.wait(1)
            self.play(Write(practice6))
            self.wait(1.5)
        
        with self.voiceover(text="Number seven: split tiers into individual services. Use microservices architecture to independently scale and deploy different components. Number eight: monitor your system and use automation tools. Implement comprehensive logging, metrics, and automated deployment pipelines.") as tracker:
            practice7 = Text("✓ Split into independent services", font_size=24, color=GREEN)
            practice7.shift(DOWN * 2.7)
            
            self.play(Write(practice7))
            self.wait(1)
            
            practice8 = Text("✓ Monitor and automate everything", font_size=24, color=GREEN)
            practice8.shift(DOWN * 3.4)
            
            self.play(Write(practice8))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Here's the complete architecture we've built together. Users connect through DNS and CDN. Load balancers distribute traffic to stateless web servers. Web servers query cache layers and message queues. Behind the scenes, we have sharded databases with replication, NoSQL for session storage, and comprehensive monitoring and automation tools. All of this runs across multiple data centers for global availability.") as tracker:
            final_title = Text("Complete Architecture", font_size=36, color=BLUE).to_edge(UP, buff=0.3)
            self.play(Write(final_title))
            
            # Simplified final architecture diagram
            # Users
            users = VGroup(
                self.create_user_icon(scale=0.3),
                self.create_user_icon(scale=0.3),
                self.create_user_icon(scale=0.3)
            ).arrange(DOWN, buff=0.3).shift(LEFT * 6 + UP * 0.5)
            users_label = Text("Users", font_size=16, weight=BOLD).next_to(users, UP, buff=0.2)
            
            # DNS + CDN
            dns_cdn = Rectangle(height=1, width=1.5, color=PURPLE, fill_opacity=0.4).shift(LEFT * 4.2 + UP * 0.5)
            dns_cdn_label = Text("DNS/CDN", font_size=12).move_to(dns_cdn.get_center())
            
            # Load Balancer
            lb = Rectangle(height=1.2, width=1.3, color=ORANGE, fill_opacity=0.4).shift(LEFT * 2.2 + UP * 0.5)
            lb_label = Text("LB", font_size=14).move_to(lb.get_center())
            
            # Web Servers
            web = Rectangle(height=1.5, width=1.2, color=GREEN, fill_opacity=0.3).shift(LEFT * 0.3 + UP * 1.2)
            web_label = Text("Web", font_size=12).move_to(web.get_center())
            
            # Cache
            cache = Rectangle(height=0.8, width=1, color=YELLOW, fill_opacity=0.4).shift(RIGHT * 1.2 + UP * 1.8)
            cache_label = Text("Cache", font_size=10).move_to(cache.get_center())
            
            # Message Queue
            mq = Rectangle(height=0.8, width=1, color=PURPLE, fill_opacity=0.4).shift(RIGHT * 1.2 + UP * 0.8)
            mq_label = Text("Queue", font_size=10).move_to(mq.get_center())
            
            # Databases (sharded)
            db1 = self.create_database_icon(color=BLUE, scale=0.25).shift(RIGHT * 3 + UP * 1.5)
            db2 = self.create_database_icon(color=BLUE, scale=0.25).shift(RIGHT * 4 + UP * 1.5)
            db_label = Text("Sharded DBs", font_size=10).shift(RIGHT * 3.5 + UP * 2.2)
            
            # NoSQL
            nosql = self.create_database_icon(color=ORANGE, scale=0.25).shift(RIGHT * 3 + UP * 0.3)
            nosql_label = Text("NoSQL", font_size=10).next_to(nosql, DOWN, buff=0.1)
            
            # Monitoring
            monitor = Rectangle(height=0.7, width=1.2, color=RED, fill_opacity=0.3).shift(RIGHT * 4.2 + UP * 0.3)
            monitor_label = Text("Monitor", font_size=10).move_to(monitor.get_center())
            
            self.play(
                FadeIn(users), Write(users_label),
                Create(dns_cdn), Write(dns_cdn_label),
                Create(lb), Write(lb_label),
                Create(web), Write(web_label),
                Create(cache), Write(cache_label),
                Create(mq), Write(mq_label),
                FadeIn(db1), FadeIn(db2), Write(db_label),
                FadeIn(nosql), Write(nosql_label),
                Create(monitor), Write(monitor_label)
            )
            
            # Connection arrows
            arrows = VGroup(
                Arrow(users.get_right(), dns_cdn.get_left(), buff=0.05, stroke_width=1.5, color=WHITE),
                Arrow(dns_cdn.get_right(), lb.get_left(), buff=0.05, stroke_width=1.5, color=WHITE),
                Arrow(lb.get_right(), web.get_left(), buff=0.05, stroke_width=1.5, color=WHITE),
                Arrow(web.get_right(), cache.get_left(), buff=0.05, stroke_width=1, color=WHITE),
                Arrow(web.get_right(), mq.get_left(), buff=0.05, stroke_width=1, color=WHITE),
                Arrow(cache.get_right(), db1.get_left(), buff=0.05, stroke_width=1, color=WHITE),
                Arrow(mq.get_right(), db2.get_left(), buff=0.05, stroke_width=1, color=WHITE)
            )
            
            self.play(Create(arrows))
            
            datacenter_label = Text("Multiple Data Centers", font_size=14, color=GREEN, weight=BOLD).shift(DOWN * 2)
            self.play(Write(datacenter_label))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Remember: scaling is an iterative process, not a one-time task. You start simple and add complexity only as needed. Monitor your system continuously. Identify bottlenecks through metrics and profiling. Address each bottleneck systematically. Test thoroughly at every stage. And always keep learning - system design evolves constantly!") as tracker:
            final_message = Text("Scaling is an Iterative Journey", font_size=36, color=YELLOW, weight=BOLD)
            final_message.shift(UP * 1.5)
            
            self.play(Write(final_message))
            self.wait(1)
            
            principles = VGroup(
                Text("• Start simple, add complexity as needed", font_size=20, color=WHITE),
                Text("• Monitor continuously", font_size=20, color=WHITE),
                Text("• Identify and fix bottlenecks", font_size=20, color=WHITE),
                Text("• Test thoroughly", font_size=20, color=WHITE),
                Text("• Keep learning and improving!", font_size=20, color=GREEN, weight=BOLD)
            ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
            principles.shift(DOWN * 0.5)
            
            for principle in principles:
                self.play(Write(principle))
                self.wait(0.8)
            
            self.wait(2)
        
        with self.voiceover(text="Thank you for joining me on this journey from zero to millions of users. You now have the knowledge to design and scale robust, high-performance systems. Keep practicing, keep building, and keep scaling. Good luck with your system design interviews and projects!") as tracker:
            self.play(FadeOut(*self.mobjects))
            
            thank_you = Text("Thank You!", font_size=60, color=BLUE, weight=BOLD)
            subtitle = Text("Keep Learning • Keep Building • Keep Scaling", font_size=28, color=GREEN)
            
            final_group = VGroup(thank_you, subtitle).arrange(DOWN, buff=0.8)
            
            self.play(Write(thank_you))
            self.play(Write(subtitle))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

    # Helper methods
    def create_user_icon(self, scale=1.0):
        head = Circle(radius=0.15 * scale, color=WHITE, fill_opacity=1)
        body = Triangle(color=WHITE, fill_opacity=1).scale(0.25 * scale)
        body.next_to(head, DOWN, buff=0.02 * scale)
        user = VGroup(head, body)
        return user

    def create_server_icon(self, scale=1.0):
        box = Rectangle(height=1 * scale, width=0.7 * scale, color=GREEN, fill_opacity=0.5)
        line1 = Line(box.get_left() + UP * 0.3 * scale, box.get_right() + UP * 0.3 * scale, color=WHITE)
        line2 = Line(box.get_left() + DOWN * 0.1 * scale, box.get_right() + DOWN * 0.1 * scale, color=WHITE)
        server = VGroup(box, line1, line2)
        return server

    def create_database_icon(self, color=BLUE, scale=1.0):
        cylinder_top = Ellipse(width=0.8 * scale, height=0.3 * scale, color=color, fill_opacity=0.6)
        cylinder_body = Rectangle(height=0.8 * scale, width=0.8 * scale, color=color, fill_opacity=0.6)
        cylinder_body.next_to(cylinder_top, DOWN, buff=0)
        cylinder_bottom = Ellipse(width=0.8 * scale, height=0.3 * scale, color=color, fill_opacity=0.6)
        cylinder_bottom.next_to(cylinder_body, DOWN, buff=0)
        
        db = VGroup(cylinder_top, cylinder_body, cylinder_bottom)
        return db
