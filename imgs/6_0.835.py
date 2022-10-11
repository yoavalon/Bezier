d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.long)
d.position_pen(0,0)
d.position_pen(3,1)
d.straight_line(Direction.SE, Length.long)

d.end()
