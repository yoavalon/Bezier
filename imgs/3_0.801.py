d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.position_pen(0,1)
d.straight_line(Direction.SE, Length.long)
d.position_pen(0,0)

d.end()
