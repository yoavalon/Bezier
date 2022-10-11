d = DslBezier()

d.position_pen(1,3)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.position_pen(0,3)
d.straight_line(Direction.SE, Length.long)

d.end()
