d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,1)

d.end()
