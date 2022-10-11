d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.short)

d.end()
