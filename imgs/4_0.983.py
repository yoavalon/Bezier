d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SE, Length.long)

d.end()
