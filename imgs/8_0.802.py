d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NW, Orient.left, Length.long, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.position_pen(1,0)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)

d.end()
