d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.long)

d.end()
