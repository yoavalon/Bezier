d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(3,2)
d.straight_line(Direction.NE, Length.long)
d.position_pen(3,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)

d.end()
