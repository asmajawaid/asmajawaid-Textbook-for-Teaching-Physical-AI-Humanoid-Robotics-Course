import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import Link from '@docusaurus/Link';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
  link: string;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Module 1: ROS 2 Core Fundamentals',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Learn the essential concepts of the Robot Operating System 2 (ROS 2), the backbone of modern robotics applications.
      </>
    ),
    link: '/docs/ros-2-basics-intro',
  },
  {
    title: 'Module 2: Vision-Language-Action (VLA) Pipeline',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Dive into the core of Physical AI by building a model that connects language commands to visual inputs and robotic actions.
      </>
    ),
    link: '/docs/vla_module',
  },
  {
    title: 'Module 3: Humanoid Kinematics and Control',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Master the principles of robot motion, from forward and inverse kinematics to trajectory planning and execution.
      </>
    ),
    link: '/docs/humanoid-kinematics-intro',
  },
  {
    title: 'Module 4: Synthetic Data and Simulation',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default, // Re-using an SVG
    description: (
      <>
        Understand the importance of simulation and synthetic data generation for training robust and reliable robotic systems.
      </>
    ),
    link: '/docs/simulation-data-intro',
  },
];

function Feature({title, Svg, description, link}: FeatureItem) {
  return (
    <div className={clsx('col col--3')}>
      <Link to={link} className={styles.featureLink}>
        <div className="text--center">
          <Svg className={styles.featureSvg} role="img" />
        </div>
        <div className="text--center padding-horiz--md">
          <Heading as="h3">{title}</Heading>
          <p>{description}</p>
        </div>
      </Link>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}