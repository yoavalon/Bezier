d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)

d.end()
