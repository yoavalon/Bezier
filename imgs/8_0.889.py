d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.long)
d.position_pen(0,3)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)

d.end()
